import random

def startGame(piles):
    filePointerUnsafe = open("unsafe", "r+")
    

    #turn = int(input("\nType 0 if you want the MACHINE to start, and 1 if YOU want to start: "))
    turn = 0
    while(True):

        unsafes = []

        for i in filePointerUnsafe:
            unsafes.append(i)

        filePointerUnsafe.seek(0)

        

        if (turn == 2):
            turn = 1
        else:
            #move = input("\nEnter the pile letter (A, B, C) and the number of chips to remove: ")
            #pile = ord(move[0]) - 65
            #numChips = int(move[2])

            computerTurn(filePointerUnsafe, piles, unsafes)

            if (piles[0] + piles[1] + piles[2] == 0):
                print("*** You LOSE! You are a WEAK little cookie! :) ***")
                break

        computerTurn(filePointerUnsafe, piles, unsafes)

        if (piles[0] + piles[1] + piles[2] == 0):
            print("*** You WON! You are a TOUGH little cookie! :) ***")
            break
            

def playerTurn(move, pile, numChips, piles):
    
    while (not (isValidMove(piles, pile, numChips))):
            print("\nOut of range! Try again.")
            move = input("\nEnter the pile letter (A, B, C) and the number of chips to remove: ")
            pile = ord(move[0]) - 65
            numChips = int(move[2])
    
    piles[pile] -= numChips

    print("\nThe human will take", numChips, "chip(s) from pile", move[0], ".")
    print("THE NUMBER OF CHIPS IN EACH PILE NOW: ")
    print("A:", piles[0], "\tB:", piles[1], "\tC:", piles[2])

def computerTurn(filePointerUnsafe, piles, unsafes):
    
    unsafeCombos = checkUnsafe(piles, unsafes)
    print(len(unsafeCombos))

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


def isValidMove(piles, pile, numChips):

    if (pile in range(0,3) and numChips in range(1, 4)):
        if (piles[pile] >= numChips):
            return True 
        else:
            return False
    else:
        return False
        


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
            print(unsafe)
    
    
    unsafes.sort()

    return unsafes

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


def main():
    #sizes = input("Enter a positive number of chips for piles A B C: ")

    sizes = str(random.randint(1, 1000)) + " " + str(random.randint(1, 1000)) + " " + str(random.randint(1, 1000))
    piles = list(map(int,sizes.split(' ')))

    #while (piles[0] < 1 or piles[1] < 1 or piles[2] < 1):
    #    print("\nInvalid piles! Try again.")
    #    sizes = input("\nEnter a positive number of chips for piles A B C: ")
    #    piles = list( map(int, sizes.split(' ')) )

    print("\nThe number of chips in each pile initially")
    print("A:", piles[0], "\tB:", piles[1], "\tC:", piles[2])



    startGame(piles)

    #if (input("Go Again? (Y/N) ") == 'Y'): main()
    main()

main()