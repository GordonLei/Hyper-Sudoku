import copy

class SudokuPuzzle():
    #constructor
    def __init__(self):
        self.coordinateValue = [[0 for i in range(9)] for j in range(9)]
        self.coordinateDomains = {}
        self.input_file = ""
        self.output_file = ""
    #create the puzzle and give it the correct input and output files
    def create_puzzle(self, inputObj, outputObj):
        input_lines = inputObj.readlines()
        for i in range(9):
            temp_num_list = input_lines[i].strip().split()
            self.coordinateValue[i] = temp_num_list
            for j in range(9):
                self.coordinateValue[i][j] = int(self.coordinateValue[i][j])
        for i in range(9):
            for j in range(9):
                if(self.coordinateValue[i][j] != 0):
                    self.coordinateDomains[str(i) + str(j)]  = []
                else:
                    self.coordinateDomains[str(i) + str(j)] = [1,2,3,4,5,6,7,8,9]
        self.input_file = inputObj
        self.output_file = outputObj

    def print_solution(self):
        for row in self.coordinateValue:
            line = " ".join(str(coord) for coord in row)
            print(line)
            self.output_file.write(line + "\n")
        print("\n")
        
    #check if this is in the overlapping regions
    def checkInOverlappingBlock(self,x,y):
            return ((0<x<4 or 4<x<8) and (0<y<4 or 4<y<8))

    #forward checking algorithm
    def forwardCheck(self, x, y, coord_value):

        #remove domains for row
        for i in range(9):
            temp_arr = self.coordinateDomains[str(x) + str(i)]
            if(int(coord_value) in temp_arr):
                temp_arr.remove(int(coord_value))
            if(len(temp_arr) == 0 and self.coordinateValue[x][i] == 0):
                return False
            if(self.coordinateValue[x][i] == self.coordinateValue[x][y] and i != y):
                return False
            self.coordinateDomains[str(x) + str(i)] = temp_arr
        
        #remove domains for column
        for i in range(9):
            temp_arr = self.coordinateDomains[str(i) + str(y)]
            if(int(coord_value) in temp_arr):
                temp_arr.remove(coord_value)
            if(len(temp_arr) == 0 and self.coordinateValue[i][y] == 0):
                return False
            if(self.coordinateValue[i][y] == self.coordinateValue[x][y] and i != x):
                return False
            self.coordinateDomains[str(i) + str(y)] = temp_arr
        
        #remove domains for non-overlapping block
        startx = x - (x % 3)
        endx = startx + 3
        starty = y - (y % 3)
        endy = starty + 3
        
        for i in range(startx, endx, 1):
            for j in range(starty, endy, 1):
                temp_arr = self.coordinateDomains[str(i) + str(j)]
                if(int(coord_value) in temp_arr):
                    temp_arr.remove(coord_value)
                if(len(temp_arr) == 0 and self.coordinateValue[i][j] == 0):
                    return False
                if(self.coordinateValue[i][j] == self.coordinateValue[x][y] and i != x):
                   return False
                self.coordinateDomains[str(i) + str(j)] = temp_arr
        
        #remove domain in overlapping block
        if (self.checkInOverlappingBlock(x,y)):
            if x <= 3:
                startx = 1
                endx = 4
            else:
                startx = 5
                endx = 8
            if y <= 3:
                starty = 1
                endy = 4
            else:
                starty = 5
                endy = 8

            for i in range(startx, endx, 1):
                for j in range(starty, endy, 1):
                    temp_arr = self.coordinateDomains[str(i) + str(j)]
                    if(int(coord_value) in temp_arr):
                        temp_arr.remove(coord_value)
                    if(len(temp_arr) == 0 and self.coordinateValue[i][j] == 0):
                        return False
                    if(self.coordinateValue[i][j] == self.coordinateValue[x][y] and i != x):
                        return False
                    self.coordinateDomains[str(i) + str(j)] = temp_arr
        return True

        
    def backwardCheck(self):
            if self.noEmptySpaces():
                return True
            coord = self.chooseNextCoordinate()
            for i in range(1,10):
                if i in self.coordinateDomains[coord[0]+coord[1]]:
                    temp = copy.deepcopy(self.coordinateDomains)
                    self.coordinateValue[int(coord[0])][int(coord[1])] = i
                    self.coordinateDomains[coord[0]+coord[1]] = []
                    for row in self.coordinateValue:
                        line = " ".join(str(coord) for coord in row)
                    if not self.forwardCheck(int(coord[0]), int(coord[1]), i):
                        self.coordinateValue[int(coord[0])][int(coord[1])] = 0
                        self.coordinateDomains = temp
                        continue
                    if self.backwardCheck():
                        return True
                    self.coordinateValue[int(coord[0])][int(coord[1])] = 0
                    self.coordinateDomains = temp
            return False
        

    def noEmptySpaces(self):
        for i in range(9):
            for j in range(9):
                if(int(self.coordinateValue[i][j]) == 0):
                    return False
        return True

    def chooseNextCoordinate(self):
        #MRV heuristic
        emptyCoordinateDomains = {key:domain for key, domain in self.coordinateDomains.items() if len(domain) > 0}
        sort_coordinate_domains = sorted(emptyCoordinateDomains.items(), key=lambda x: len(x[1]))
        
        tempLength = len(sort_coordinate_domains[0][1])
        tempArray = []
       
        for elem in sort_coordinate_domains:
            if(len(elem[1]) == tempLength):
                tempArray.append(elem[0])
            else:
                break 
            
        #Degree heuristic
        tempArrayUnassignedNeighborNum = []
        for coord in tempArray:
            coord_x = int(coord) % 10
            coord_y = int(coord) // 10
            counter = 0
            #columns
            checked_coord_ls = []
            for i in range(9):
                if coord_x != i and self.coordinateValue[coord_x][i] == 0:
                    checked_coord_ls.append((coord_x, i))
                    counter+=1
            #rows            
            for i in range(9):
                if coord_y != i and self.coordinateValue[i][coord_y] == 0:
                    checked_coord_ls.append((i, coord_y))
                    counter+=1
            #non-overlapping block
            startx = coord_x  - (coord_x  % 3)
            endx = startx + 3
            starty = coord_y  - (coord_y % 3)
            endy = starty + 3
            for i in range(startx, endx, 1):
                for j in range(starty, endy, 1):
                    if (i,j) not in checked_coord_ls and self.coordinateValue[i][j] == 0:
                            counter+=1
            #overlapping block
            if (self.checkInOverlappingBlock(coord_x, coord_y)):
                if coord_x <= 3:
                    startx = 1
                    endx = 4
                else:
                    startx = 5
                    endx = 8
                if coord_y <= 3:
                    starty = 1
                    endy = 4
                else:
                    starty = 5
                    endy = 8
              
                for i in range(startx, endx, 1):
                    for j in range(starty, endy, 1):
                        if (i,j) not in checked_coord_ls and self.coordinateValue[i][j] == 0:
                                counter+=1
            tempArrayUnassignedNeighborNum.append((coord,counter))
        sort_UNN = sorted(tempArrayUnassignedNeighborNum, key=lambda x: x[1], reverse=True)
        return (sort_UNN[0][0][0], sort_UNN[0][0][1])

    def solve_puzzle(self):
        for i in range(9):
            for j in range(9):
                if self.coordinateValue[i][j] != 0:      
                    if not (self.forwardCheck(i,j, self.coordinateValue[i][j])):
                        self.output_file.write("The puzzle is unsolvable!" + "\n")
                        quit()
                        
        self.backwardCheck()
        self.print_solution()

i1= open("Input1.txt", "r")
o1 = open("Output1.txt", "w+")
i2= open("Input2.txt", "r")
o2 = open("Output2.txt", "w+")
i3= open("Input3.txt", "r")
o3 = open("Output3.txt", "w+")
i4= open("Input4.txt", "r")
o4 = open("Output4.txt", "w+")

i5= open("Input5.txt", "r")
o5 = open("Output5.txt", "w+")

solver = SudokuPuzzle()
solver.create_puzzle(i1, o1)
solver.solve_puzzle()
solver.create_puzzle(i2, o2)
solver.solve_puzzle()
solver.create_puzzle(i3, o3)
solver.solve_puzzle()
solver.create_puzzle(i4, o4)
solver.solve_puzzle()
solver.create_puzzle(i5, o5)
solver.solve_puzzle()

i1.close()
o1.close()
i2.close()
o2.close()
i3.close()
o3.close()
i4.close()
o4.close()
i5.close()
o5.close()

#go through text file
#insert in dictionary all the coordinates and the default [1-9] domain list
#Go back to coordinates with pre-set values, run forward checking with them
#return false if any coordinate with zero domain comes up




