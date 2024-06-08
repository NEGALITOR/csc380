from diag import Dialogue

# Main Function
def main():

    print("Hello, my name is Eliza!")
    fileName = "dialogue.txt"
    diag = Dialogue(fileName)

    diag.stripFileInfo()

    while (True):

        userInput = diag.getInput()
        keyWord = diag.getKeyWord(userInput)

        print(diag.getResp(keyWord))
        

main()