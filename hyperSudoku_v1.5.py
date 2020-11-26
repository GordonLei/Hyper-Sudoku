class sudokuPuzzle():
    #constructor
    def __init__(self):
        self.coordinateValue = [[0 for i in range(9)] for j in range(9)]
        self.coordinateDomains = {}
        self.input_file = ""
        self.output_file = ""
    #create the puzzle and give it the correct input and output files
    def create_puzzle(self, inputObj, outputObj):
        #coordinateArray = []
        input_lines = inputObj.readlines()
        for i in range(9):
            temp_num_list = input_lines[i].strip().split()
            #coordinateArray.append(temp_num_list)
            self.coordinateValue[i] = temp_num_list
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
            line = " ".join(row)
            print(line)
            self.output_file.write(line + "\n")
    #check if this is in the overlapping regions
    def checkInOverlappingBlock(self,x,y):
            return ((0<x<=3 or 3<x<=7) and (0<y<=3 or 3<y<=7))
    #forward checking algorithm
    def forwardCheck(self, x, y, coord_value):
            #remove domains for row
            for i in range(9):
                temp_arr = self.coordinateDomains[str(x) + str(i)]
                temp_arr.remove(coord_value)
                #remember to check if list is empty
        if(len(temp_arr) == 0):
            return False
            
                self.coordinateDomains[str(x) + str(i)] = temp_arr
            
            #remove domains for column
            for i in range(9):
                temp_arr = self.coordinateDomains[str(i) + str(y)]
                temp_arr.remove(coord_value)
        if(len(temp_arr) == 0):
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
                    temp_arr.remove(coord_value)
        if(len(temp_arr) == 0):
            return False
                    self.coordinateDomains[str(i) + str(j)] = temp_arr
            
            #remove domain in overlapping block
            if (self.checkInOverlappingBlock(x,y)):
                startx = x - (x % 3) + 1
                endx = startx + 3
                starty = y - (y % 3) + 1
                endy = starty + 3
                for i in range(startx, endx, 1):
                    for j in range(starty, endy, 1):
                            temp_arr = self.coordinateDomains[str(i) + str(j)]
                            temp_arr.remove(coord_value)
            if(len(temp_arr) == 0):
            return False
                            self.coordinateDomains[str(i) + str(j)] = temp_arr

return True
    def backwardCheck(self):
            if self.noEmptySpaces():
                    return True
            coord = self.chooseNextCoordinate()
        for i in range(1,10):
            if i in self.coordinateDomains[str(coord[0])+str(coord[1])]:
                self.coordinateValue[coord[0]][coord[1]] = i
                if self.backwardCheck():
                        return True
                self.coordinateValue[coord[0]][coord[1]] = 0
        return False
        

    def noEmptySpaces(self):
        for i in range(9):
            for j in range(9):
                if(self.coordinateValue[i][j] == 0)
                    return False
        return True

    def chooseNextCoordinate(self):
        #MRV heuristic
        sort_coordinate_domains = sorted(self.coordinate_domains.items(), key=lambda x: len(x[1]))
        tempLength = len(sort_coordinate_domains[0][1])
        tempArrray = []
        i = 0
        while(true):
            if(sort_coordinate_domains[i][1] == tempLength):
                tempArrray.append(sort_coordinate_domains[i][0])
            Else:
                Break 

        #Degree heuristic
    tempArrayUnassignedNeighborNum = []
    
    For coord in tempArray
        coord_x = int(coord) % 10
        coord_y = int(coord) / 10
        counter = 0
        #columns
        checked_coord_ls = []
        for i in range(9):
            if coord_x != i and self.coordinateValue[elem[0]] [i] == 0:
                checked_coord_ls.append((elem[0], i))
                counter++
#rows            
for i in range(9):
            if coord_y != i and self.coordinateValue[i] [elem[1]] == 0:
        checked_coord_ls.append((i, elem[1]))
                counter++
        
        #non-overlapping block
        startx = x - (x % 3)
            endx = startx + 3
            starty = y - (y % 3)
            endy = starty + 3
    for i in range(startx, endx, 1):
                for j in range(starty, endy, 1):
            if (i,j) not in checked_coord_ls and self.coordinateValue[i] [j] == 0:
                    counter++
    
    #overlapping block
    if (self.checkInOverlappingBlock(coord_x, coord_y):
                startx = x - (x % 3) + 1
                endx = startx + 3
                starty = y - (y % 3) + 1
                endy = starty + 3
        for i in range(startx, endx, 1):
                    for j in range(starty, endy, 1):
                if (i,j) not in checked_coord_ls and self.coordinateValue[i] [j] == 0:
                        counter++
        
tempArrayUnassignedNeighborNum.append((coord,counter))

sort_UNN = sorted(tempArrayUnassignedNeighborNum, key=lambda x: x[1], reverse=True)
return (sort_UNN[0][0], sort_UNN[0][1])



    

def solve_puzzle(self):
    for i in range(9):
for j in range(9):
if self.coordinateValue[i][j] != 0:
if(!self.forwardCheck()):
    self.output_file.write(“The puzzle is unsolvable!” + "\n")
if !backwardCheck():
     self.output_file.write(“The puzzle is unsolvable!” + "\n")
else:
    self.print_solution()

i1= open("Input1.txt", "r")
o1 = open("Output1.txt", "w+")

solver = SudokuPuzzle()
solver.create_puzzle(i1, o1)
solver.solve_puzzle()
i1.close()
o1.close()

#go through text file
#insert in dictionary all the coordinates and the default [1-9] domain list
#Go back to coordinates with pre-set values, run forward checking with them
#return false if any coordinate with zero domain comes up




