class sudokuPuzzle():
    #constructor 
    def __init__(self):
        self.coordinateValue = [[0 for i in range(9)] for j in range(9)]
        self.coordinateDomains = {}
    #
    def checkInOverlappingBlock(self,x,y):
        return ((0<x<=3 or 3<x<=7) and (0<y<=3 or 3<y<=7))
    #
    def forwardCheck(self, x, y, coord_value):
        if coord == 0:
            return
        else: #elif:
            #remove domains for row
            for i in range(9):
                temp_arr = self.coordinateDomains[str(x) + str(i)]
                temp_arr.remove(coord_value)
                #remember to check if list is empty
                self.coordinateDomains[str(x) + str(i)] = temp_arr
            
            #remove domains for column
            for i in range(9):
                temp_arr = self.coordinateDomains[str(i) + str(y)]
                temp_arr.remove(coord_value)
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
                                self.coordinateDomains[str(i) + str(j)] = temp_arr
    def backwardCheck(self):
        if self.noEmptySpaces():
            return True
        coord = self.chooseNextCorrdinate()
        for i in range(1,10):
            if i in self.coordinateDomains[str(coord[0])+str(coord[1])]:
                self.coordinateValue[coord[0]][coord[1]] = i
                if self.backwardCheck():
                    return True
                self.coordinateValue[coord[0]][coord[1]] = 0
        return False
    
    def chooseNextCoordinate(self):
        #MRV heuristic
        #Degree heuristic
        return
    def hyperSudoku(self):
        return
    def forwardChecking(self):
        return
    def backwardChecking(self):
        return
    

input_file = open("Sample_Input.txt", "r")
coordinateArray = []
for line in input_file:
    temp_num_list = line.strip().split()
    coordinateArray.append(temp_num_list)

#go through text file
#insert in dictionary all the coordinates and the default [1-9] domain list
#Go back to coordinates with pre-set values, run forward checking with them
#return false if any coordinate with zero domain comes up

