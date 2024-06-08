# ----------------------------------------------------------------------------------
# In:   piles - The initial pile counts are fed in by user
# Out:  
# Maintains the logic of the game such as turns and unsafe initial reading
# ----------------------------------------------------------------------------------
def startGame(piles):
    filePointerUnsafe = open("unsafe", "r+")
    turn = int(input("\nType 0 if you want the MACHINE to start, and 1 if YOU want to start: "))

    while(True):

        unsafes = []

        for i in filePointerUnsafe:
            unsafes.append(i)

        filePointerUnsafe.seek(0)

        if (turn == 0):
            turn = 1
        else:
            

            playerTurn(piles)

            if (piles[0] + piles[1] + piles[2] == 0):
                print("*** You LOSE! You are a WEAK little cookie! :) ***")
                break

        computerTurn(filePointerUnsafe, piles, unsafes)

        if (piles[0] + piles[1] + piles[2] == 0):
            print("*** You WON! You are a TOUGH little cookie! :) ***")
            break
            
# ----------------------------------------------------------------------------------
# In:   piles - The pile counts are fed in to manipulate the values by the player
# Out:  
# Performs the players turn
# If the move is not valid (checks with isValidMove()), it will require the user to renter
# Subtracts pile by the numChips
# ----------------------------------------------------------------------------------
def playerTurn(piles):

    move = input("\nEnter the pile letter (A, B, C) and the number of chips to remove: ")
    pile = ord(move[0]) - 65
    numChips = int(move[2])

    while (not (isValidMove(piles, pile, numChips))):
            print("\nOut of range! Try again.")
            move = input("\nEnter the pile letter (A, B, C) and the number of chips to remove: ")
            pile = ord(move[0]) - 65
            numChips = int(move[2])
    
    piles[pile] -= numChips

    print("\nThe human will take", numChips, "chip(s) from pile", move[0], ".")
    print("THE NUMBER OF CHIPS IN EACH PILE NOW: ")
    print("A:", piles[0], "\tB:", piles[1], "\tC:", piles[2])

# ----------------------------------------------------------------------------------
# In:   filePointerUnsafe - utilized to traverse the unsafe file
#       piles - The pile counts are fed in to manipulate the values by the player
#       unsafes - list of unsafe combinations
# Out:  
# Manages computer behavior when presented with the pile values
# Writes the sorted unsafes (done in computerMove()) to the unsafe files
#
# ----------------------------------------------------------------------------------
def computerTurn(filePointerUnsafe, piles, unsafes):
    
    unsafeCombos = checkUnsafe(piles, unsafes)

    if (len(unsafeCombos) != 0):
        unsafes = addUnsafe(piles, unsafes)

        for i in unsafes:
            filePointerUnsafe.write(i)
        
        filePointerUnsafe.seek(0)
    
    move = []
    move = computerMove(piles, unsafeCombos)

    print("\nI take", move[1], "from pile", chr(move[0] + 65), ".")

    piles[move[0]] -= move[1]

    print("The number of chips in each pile after the computer moves is:")
    print("A:", piles[0], "\tB:", piles[1],"\tC:", piles[2])

# ----------------------------------------------------------------------------------
# In:   piles - The piles and their values
#       pile - pile letter
#       numChips - number taken away from pile
# Out:  True or False whether the amount taken is valid and which pile
# ----------------------------------------------------------------------------------
def isValidMove(piles, pile, numChips):

    if (pile in range(0,3) and numChips in range(1, 4)):
        if (piles[pile] >= numChips):
            return True 
        else:
            return False
    else:
        return False
        

# ----------------------------------------------------------------------------------
# In:   piles - The piles and their values
#       unsafes - list of all unsafe values
# Out:  the unsafe combinations possible with the current arrangement of the piles
# Compares all possible next unsafes to determine what the next move should be
# ----------------------------------------------------------------------------------
def checkUnsafe(piles, unsafes):
    unsafeCombos = []
    
    for i in range(3, 0, -1):
        for j in range(0, 3):

            next = piles[j] - i

            if (next < 0): next = 0

            if (j == 0): check = str(next) + " " + str(piles[1]) + " " + str(piles[2]) + "\n"
            if (j == 1): check = str(piles[0]) + " " + str(next) + " " + str(piles[2]) + "\n"
            if (j == 2): check = str(piles[0]) + " " + str(piles[1]) + " " + str(next) + "\n"

            if (unsafes.count(check) > 0 and unsafeCombos.count(check) == 0): unsafeCombos.append(check)

    return unsafeCombos

# ----------------------------------------------------------------------------------
# In:   piles - The piles and their values
#       unsafes - list of all unsafe values
# Out:  the unsafe combinations possible with the current arrangement of the piles
# Adds previous unsafe if the unsafe does not exist in the unsafes list
# ----------------------------------------------------------------------------------
def addUnsafe(piles, unsafes):
    unsafe = str(piles[0]) + " " + str(piles[1]) + " " + str(piles[2]) + "\n"

    if (unsafes.count(unsafe) == 0): unsafes.append(unsafe)
    
    for i in range(1,4):
        for j in range(0, 3):

            prev = piles[j] + i

            if (j == 0): unsafe = str(prev) + " " + str(piles[1]) + " " + str(piles[2]) + "\n"
            if (j == 1): unsafe = str(piles[0]) + " " + str(prev) + " " + str(piles[2]) + "\n"
            if (j == 2): unsafe = str(piles[0]) + " " + str(piles[1]) + " " + str(prev) + "\n"

            if (unsafes.count(unsafe) == 0): unsafes.append(unsafe)

    unsafes.sort()
    return unsafes

# ----------------------------------------------------------------------------------
# In:   piles - The initial pile counts are fed in by user
#       unsafeCombos - the unsafe combinations possible with the current arrangement of the piles
# Out:  the move that the computer will perform
# Checks if a move is valid (with isValidMove())
# If there arent any unsafe combos then immediately append to move list
# If unsafe combos exist then predict next moves and check if any of those exist in the unsafecombos
# If not moves are found, cycle through until a valid move appears and perform it
# ----------------------------------------------------------------------------------
def computerMove(piles, unsafeCombos):

    move = []
    
    for i in range (3, 0, -1):
        for j in range (0, 3):
            if (not(isValidMove(piles, j, i))):
                pass
            else:
                if (len(unsafeCombos) == 0):
                    move.append(j)
                    move.append(i)
                    return move
                else:
                    if (j == 0): next = str(piles[0] - i) + " " + str(piles[1]) + " " + str(piles[2]) + "\n"
                    if (j == 1): next = str(piles[0]) + " " + str(piles[1] - i) + " " + str(piles[2]) + "\n"
                    if (j == 2): next = str(piles[0]) + " " + str(piles[1]) + " " + str(piles[2] - i) + "\n"

                    if (unsafeCombos.count(next) == 0):
                        move.append(j)
                        move.append(i)
                        return move
                    
    for i in range (3, 0, -1):
        for j in range (0, 3):
            if (isValidMove(piles, j, i)):
                move.append(j)
                move.append(i)
                return move

# ----------------------------------------------------------------------------------
# Main
# gets input from user and initializes game
# ----------------------------------------------------------------------------------
def main():
    sizes = input("Enter a positive number of chips for piles A B C: ")
    piles = list(map(int,sizes.split(' ')))

    while (piles[0] < 1 or piles[1] < 1 or piles[2] < 1):
        print("\nInvalid piles! Try again.")
        sizes = input("\nEnter a positive number of chips for piles A B C: ")
        piles = list( map(int, sizes.split(' ')) )

    print("\nThe number of chips in each pile initially")
    print("A:", piles[0], "\tB:", piles[1], "\tC:", piles[2])



    startGame(piles)

    if (input("Go Again? (Y/N) ") == 'Y'): main()

main()