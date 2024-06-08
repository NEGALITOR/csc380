import random
import sys
import os
import time
from copy import copy, deepcopy
import re

# Main
    # Creates a grid using a lists of lists
    # Utilize a switch to determine arguments
    # Asks for user input for num gens and simulates
def main(args):
    grid = [[ [0, 0] for i in range(0, 20)] for j in range(0, 20)]
    prompt = '\033[0m' + "\nInitial Random Colony Prior to Evolution\n" + "************************************************"


    if len(args) < 2:
        randomize(grid)
    else:
        match args[1]:
            case '-f':
                prompt = '\033[0m' + "\nInitial File Colony Prior to Evolution\n" + "************************************************"
                getState(grid, args[2])
            case '-help':
                print('\033[0m' + "\n-help\tDisplay command list"
                    + "\n-f filename\tUse evolution -f filename.txt for file input" 
                    + "\n-g\tGame of Life w/o generational death")
            case _:
                print('\033[0m' + "Invalid argument\n" 
                    + "For further help use -help")
                sys.exit()


        
    print('\033[0m' + "Artificial Life Simulation of Game of Life\n\n"
            + "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n"
            + "Each cell with one or no neighbors dies, as if by loneliness.\n"
            + "Each cell with four or more neighbors dies, as if by overpopulation.\n"
            + "Each cell with two or three neighbors survives.\n"
            + "Each cell with three neighbors becomes populated.\n"
            + "Each cell that ages over 10 generations dies.\n\n")

    gens = input("How many generations would you like to simulate? ")

    print(prompt)
    printGrid(grid)

    for i in range(1, int(gens)+1):
        #os.system('clear')
        grid = gameOfLife(grid)
        print('\033[0m' + "How Colony Has Evolved After " + str(i) + " Generation(s)\n"
              + "************************************************")
        printGrid(grid)
#        time.sleep(1)

# Start the Game of Life simulation
    # Gets amount and values of neighbors
    # Empties and resetting age if cell "dies"
    # Increment age if conditions are met
    # Populates and ages if overcrowded
# Returns the grid
def gameOfLife(grid):
    nextGrid = deepcopy(grid)

    for i in range(0, 20):
        for j in range(0, 20):
            neighborVals = neighborCheck(grid, i, j)
            numNeighbors = neighborVals.count(1)

            if (numNeighbors < 2 or numNeighbors > 3 or grid[i][j][1] > 10):
                nextGrid[i][j][0] = 0
                nextGrid[i][j][1] = 0
            elif (numNeighbors == 2 and grid[i][j][0] == 1):
                nextGrid[i][j][1] += 1
            elif(numNeighbors == 3):
                nextGrid[i][j][0] = 1
                nextGrid[i][j][1] += 1

    grid = deepcopy(nextGrid)
    return grid

# Returns list of neighboring cells for usage in Game of Life
    # Creates an array of values from the neighbors
    # Populates with every value around a cell
# Returns the neighborVal array
def neighborCheck(grid, row, col):
    neighborVal = []

    # Top Left
    if (row == 0 and col == 0):
        neighborVal.extend([grid[0][1][0],
                           grid[1][0][0],
                           grid[1][1][0]])
    # Top Right
    elif (row == 0 and col == 19):
        neighborVal.extend([grid[0][18][0],
                           grid[1][19][0],
                           grid[1][18][0]])
    # Bottom Left
    elif (row == 19 and col == 0):
        neighborVal.extend([grid[19][1][0],
                           grid[18][0][0],
                           grid[18][1][0]])
    # Bottom Right
    elif (row == 19 and col == 19):
        neighborVal.extend([grid[19][18][0],
                           grid[18][19][0],
                           grid[18][18][0]])
    # Top Row
    elif (row == 0):
        neighborVal.extend([grid[0][col+1][0],
                           grid[0][col-1][0],
                           grid[1][col][0],
                           grid[1][col+1][0],
                           grid[1][col-1][0]])
    # Bottom Row
    elif (row == 19):
        neighborVal.extend([grid[19][col+1][0],
                           grid[19][col-1][0],
                           grid[18][col][0],
                           grid[18][col+1][0],
                           grid[18][col-1][0]])
    # Left Column
    elif (col == 0):
        neighborVal.extend([grid[row][1][0],
                           grid[row+1][0][0],
                           grid[row+1][1][0],
                           grid[row-1][0][0],
                           grid[row-1][1][0]])   
    # Right Column
    elif (col == 19):
        neighborVal.extend([grid[row][18][0],
                           grid[row+1][19][0],
                           grid[row+1][18][0],
                           grid[row-1][19][0],
                           grid[row-1][18][0]])   
    # Middle
    else:
        neighborVal.extend([grid[row][col+1][0],
                           grid[row][col-1][0],
                           grid[row-1][col][0],
                           grid[row-1][col+1][0],
                           grid[row-1][col-1][0],
                           grid[row+1][col][0],
                           grid[row+1][col+1][0],
                           grid[row+1][col-1][0]])
    return neighborVal

# Reads in the file Grid State
    # Reads the provided file and removes every space and \n
    # Sets the grid values based on the chars fed in
def getState(grid, fileName):
    try:
        readFile = open(fileName, 'r')
    except FileNotFoundError:
        print('\033[0m' + "File Does Not Exist")
        sys.exit()
    
    fileGrid = readFile.read()
    readFile.close()

    fileGrid = re.sub(r"[\n\s]*", "", fileGrid)
    #print(fileGrid)

    iFile = 0
    for i in range(0, 20):
        for j in range(0, 20):
            char = fileGrid[iFile]
            iFile += 1
            
            if (char == "0"):
                grid[i][j][0] = 0
            elif (char == 'X'):
                grid[i][j][0] = 1
            else:
                print("typo in file")
                sys.exit()


# Randomizes Grid if no arg is given
def randomize(grid):
    for i in range (0, 20):
        for j in range (0, 20):
            grid[i][j][0] = random.randint(0, 1)	
            if (grid[i][j][0] == 1):
                grid[i][j][1] = 1

# Prints Grid
def printGrid(grid):
    for i in range (0, 20):
        for j in range (0, 20):
            if (grid[i][j][0] == 1):
                print('\033[34m' + 'X', end=' ')
            else:
                print('\033[0m' + '0', end=' ')
        print()
    print()



main(sys.argv)