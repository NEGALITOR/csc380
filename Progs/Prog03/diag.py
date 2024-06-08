import random

class Dialogue:

    # Initializes Dialogue Constructor
    def __init__(self, filename):
        
        self.filename = filename
        self.respArr = {}
        self.inputString = ""
        self.keyPhrases = {"always",
                           "because",
                           "sorry",
                           "maybe",
                           "i think",
                           "you",
                           "yes",
                           "no",
                           "i am",
                           "i'm",
                           "i feel",
                           "family",
                           "mother",
                           "mom",
                           "dad",
                           "father",
                           "sister",
                           "brother",
                           "husband",
                           "wife",
                           "dream",
                           "nightmare"
                        }
        self.stopWords = {"this",
                          "that",
                          "take",
                          "want",
                          "which",
                          "then",
                          "than",
                          "will",
                          "with",
                          "have",
                          "after",
                          "such",
                          "when",
                          "some",
                          "them",
                          "could",
                          "make",
                          "through",
                          "from",
                          "were",
                          "also",
                          "into",
                          "they",
                          "their",
                          "there"
                        }
        
    # Grab info from file and section according to responses and fill up respArr disctionary
    def stripFileInfo(self):
    
        fileIn = open(self.filename, 'r')
        lines = fileIn.readlines()
        fileIn.close()

        resps = []

        while (lines):
            key = lines.pop(0).strip('\n')
            #print(key)
            key = key.strip()
            

            while (lines[0] != "#\n"):
                resps.insert(0, lines.pop(0).strip('\n').strip())
                
            #print(resps)

            if (key.rfind('|') != 1):
                secKeys = key.split('|')
                for secKey in secKeys:
                    self.respArr.update({secKey: resps.copy()})
            else:
                self.respArr.update({key: resps.copy()})
            #print(self.respArr)

            resps.clear()
            lines.pop(0)

            
    # Cleans up string for utilization from the input
    def clean(self, stringIn):

        for ch in stringIn:
            if ((ch.isalnum() or ch.isspace()) == False):
                stringIn = stringIn.replace(ch, "")
            
            self.inputString = stringIn


        for word in stringIn:
            if word in self.stopWords:
                stringIn = stringIn.replace(word, "")
        return stringIn
    
    # Manages input logic
    def getInput(self):
        
        stringIn = input(" >> ")
        if (stringIn.strip() == "bye"):
            print("Have a great day!")
            exit()

        stringIn = stringIn.lower()

        stringIn = self.clean(stringIn)

        return stringIn
    
    # Gets the keyword and matches it with the Dialogue dictionary to see if there is a match
    def getKeyWord(self, stringIn):
        
        keyWord = "__NO_MATCH__"
        wordsIn = stringIn.split()
        index = -1
            

        #print(wordsIn)
        #print()
        for word in wordsIn:           
            #print(word)
            #print()

            #print(wordsIn)
            if (word == "joke"):
                keyWord = "joke"
                joke()
                return keyWord
            
            if (word == "peanut"):
                keyWord = "peanut"
                peanut()
                return keyWord


            if word in self.respArr.keys():
                
                keyWord = word
                index = stringIn.index(word)
                break
        
        for key in self.keyPhrases:
            if key in stringIn and stringIn.index(key) < index:
                keyWord = key
                break

        return keyWord
    
    # Gets the response needed to reply including * substitution
    def getResp(self, keyWord):

        if (keyWord == "joke" or keyWord == "peanut"):
            return ""

        respList = self.respArr[keyWord]
        resp = random.choice(respList)

        if (resp.find('*') != -1):

            splitIn = self.inputString.split(keyWord)
            subSplit = splitIn[1].strip()

            resp = resp.replace('*', subSplit)

        return resp
    
# Tells a bad joke
def joke():
    print("What does a baby computer call their father?")
    print("Data.", end =" ")

# Gives you a peanut
def peanut():
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
          +"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⠤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
          +"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⣔⣾⡅⡼⣤⡊⣤⣤⠀⢬⣽⣶⡤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
          +"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡏⣺⠏⢸⢳⠁⠈⣷⠘⠘⣷⡀⠹⡄⠙⢾⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
          +"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⡝⠀⠉⠀⡼⠀⠀⢀⡚⢀⣂⣻⢆⣃⣹⣄⣈⢳⡙⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
          +"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠋⠚⠚⢃⣛⣻⢁⣉⣁⣅⣧⢨⡥⢭⣠⡤⠬⣣⣼⢧⣿⣍⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
          +"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣇⣿⢻⣻⣼⡏⢹⣤⢏⠄⠀⢹⡾⠀⠈⣿⡇⠀⢙⣇⠀⠹⣟⢾⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
          +"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⢃⡏⢈⣿⠏⡄⠈⣟⠀⠀⢀⠸⠄⠀⠀⠹⠅⠀⠈⢿⠀⢦⣹⠀⠹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
          +"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⢸⠁⢸⣞⣀⣀⣗⢃⣀⠀⣬⣰⢆⡧⠤⠰⠠⡤⠄⢼⢧⠠⢄⢲⣀⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
          +"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⢼⣃⣫⣽⣛⠣⣗⡲⢴⣶⠶⠒⢲⡔⠷⠶⢶⣴⠿⣿⡛⢚⣲⢾⡾⣷⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
          +"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⣟⡿⣥⣿⣶⣿⣿⠻⢿⣮⣷⡀⢈⣿⠇⡰⢫⣷⡿⠟⣿⣿⣯⣿⣿⡇⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
          +"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡾⢱⣿⣿⡿⢿⣿⣧⠀⠘⢻⢳⠑⣿⡼⢰⣿⠋⠀⢰⣿⣿⣿⡿⣿⡹⡄⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
          +"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⡇⣿⣿⣿⣿⣾⣿⣿⡆⠀⢸⣾⣿⡏⣧⣿⢿⠀⠀⢸⣿⣿⣿⣷⣿⡇⡇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
          +"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⣷⡹⣿⣿⣿⣿⣿⠟⣀⡤⢾⡾⠿⣷⡿⣝⢿⣦⣀⠘⣿⣿⣿⣿⡿⣰⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
          +"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡏⣿⠷⣿⣭⣿⣿⣿⣋⣵⠫⠀⢀⣿⡆⠈⠳⣝⣿⢿⣿⣯⡙⣛⣻⠋⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
          +"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡏⡸⢧⣰⣿⠖⡶⢿⠛⠚⠓⠒⠋⠈⣟⣒⡒⢋⣞⣒⣛⡟⣛⣿⢳⠀⣽⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
          +"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⣷⣼⠟⣶⣿⠿⢿⣄⡿⠛⠛⠿⣷⠛⠛⠹⡟⠛⠉⢹⣼⢟⣿⠛⢢⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
          +"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⢹⡄⠹⡏⠀⢘⢿⡀⠀⠀⠀⠛⠀⠀⠀⠇⠀⠀⠘⠛⠘⠈⠀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
          +"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡈⢷⠀⢻⡀⠘⢈⢧⠠⠀⡀⣰⠀⠀⠀⡀⢀⠀⡤⠀⢠⠃⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
          +"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⢺⣿⣇⢐⣸⣱⢀⣻⢠⣛⣋⣙⣻⣀⣀⣚⣹⣀⣆⢁⣄⡸⣧⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
          +"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⣾⡵⢞⣫⣽⠸⡏⢹⡾⠛⢻⣟⠿⠉⠙⣿⡟⠉⣻⣿⠈⠘⣟⠉⡇⣿⣏⠻⢿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
          +"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⡫⢜⣯⣴⠿⠑⣾⢰⠃⠘⠛⠀⢘⡋⠀⠀⠀⣹⠄⠀⠈⣇⠀⠀⢻⡄⢿⠸⡝⢿⣦⣹⡎⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
          +"⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⢀⣼⠟⣱⣿⠟⠁⠀⡼⢹⠀⢰⣣⠃⠠⠋⠈⠀⠀⠰⠀⠀⢀⠆⠀⠀⣀⡈⠹⣜⡂⢱⡀⠙⣿⣿⣌⣿⣄⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀\n"
          +"⠀⠀⠀⠀⠀⠀⠀⢰⡏⠀⠀⠘⠛⠾⢿⣾⣿⣏⠀⠀⢠⠁⣼⠾⢸⣇⣧⡾⣿⢰⠇⡘⠹⣧⡿⠏⠋⣷⡏⠉⢻⡂⠀⢧⠸⣧⠀⠈⢻⣿⣾⣿⡖⠊⠉⠁⠉⢳⡀⠀⠀⠀⠀⠀\n"
          +"⠀⠀⠀⠀⠀⠀⠀⣘⡦⢄⡀⠀⠀⠀⢄⣈⠉⠉⠙⠲⣿⠀⡟⠀⢸⣿⠋⠀⣿⣼⠘⠀⠀⠸⠃⠀⠀⢹⠇⠀⠈⡿⠀⣼⡇⠻⡗⠊⠑⠻⠛⠃⠁⠰⠒⠀⣀⣼⠁⠀⠀⠀⠀⠀\n"
          +"⠀⠀⠀⠀⠀⡠⠊⠀⠀⠀⠉⠀⠐⠒⠤⣀⣀⣀⡀⢸⢋⢨⠃⠀⣼⠋⠘⠀⣜⠃⠀⠀⠰⢸⢀⠄⠀⢈⢃⣀⣀⣿⢔⣼⡿⣆⢹⠀⠀⠀⣀⡠⠤⠂⠀⠀⠀⠀⠉⠢⡀⠀⠀⠀\n"
          +"⠀⠀⠀⠀⡔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡏⣾⡋⡛⡛⠋⣛⣛⣻⡃⣘⣉⣉⣉⣛⢘⣋⣉⣀⢘⣥⣤⣿⢨⣤⣧⡿⣶⡏⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⡄⠀⠀\n"
          +"⠀⠀⢀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⣧⠋⣿⠋⠉⣿⡏⠉⢹⣷⠈⠀⠀⠀⢹⣿⡅⠀⢹⡇⠀⠈⢹⡆⠀⢸⠁⢸⡇⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀\n"
          +"⠀⠀⡜⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠈⠑⠢⣴⠿⣿⡀⣟⠀⠀⡝⢇⠀⠈⠋⠀⡀⠀⠀⠘⡟⠀⠀⠀⡁⠀⠀⠈⡁⠀⠈⠀⠈⣷⣄⡤⠒⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄\n"
          +"⠀⠀⡇⠀⠀⠀⠀⠀⢠⣄⣉⠢⢄⠀⠀⠀⠀⠈⢧⣇⢳⡼⡀⣀⡜⣈⣰⣬⡶⠀⢁⡀⢀⣰⢃⣀⡄⣤⡎⡠⠀⠼⢡⠶⢻⡀⢁⣿⠃⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⡆\n"
          +"⠀⠀⢱⠀⠀⠀⠀⠐⠁⠂⠈⢉⠒⡦⣄⣀⣀⡤⠋⢸⡤⢴⡷⡬⣧⣿⠷⢶⣧⢠⠴⠶⠶⣶⣸⡾⠒⢾⣶⡗⠒⢿⠸⠒⣿⠃⣸⠙⠂⣀⣀⣀⣠⠴⠒⠉⠀⠉⠂⠀⠀⠀⢀⡇\n"
          +"⠀⠀⠀⠳⣄⠀⠀⠀⠀⠀⠀⢸⣆⠳⣀⡀⠈⠙⠒⠦⢿⡈⣧⠰⠸⡯⡇⡀⢹⡏⣄⠀⠀⠈⡇⠀⠀⢸⡏⠁⠀⣾⠁⢀⡏⢠⠿⠒⠭⠁⠀⣨⠇⡼⠀⠀⠀⠀⠀⠀⠀⣠⠞⠀\n"
          +"⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠈⢧⣀⡉⠙⠒⠲⢄⡘⣇⡈⢳⠶⣟⠿⠤⢴⠃⠼⠦⠴⠂⢻⠦⠀⢚⡵⡆⢘⢃⣚⠃⢀⣟⡠⠖⠒⠚⠉⣀⡴⠃⠀⠀⠀⠀⠀⣠⠎⠀⠀⠀\n"
          +"⠀⠀⠀⠀⠀⠀⠈⠢⣀⠀⠀⠀⠀⠀⠀⠹⣦⢀⣀⠀⠉⢿⣆⢺⡟⠲⣦⠖⠲⣦⡰⠒⠒⢾⡗⠛⠛⢿⠘⠉⣹⡟⢩⢧⠞⠉⠀⢀⡀⣰⠋⠀⠀⠀⠀⠀⠀⣀⠔⠁⠀⠀⠀⠀\n"
          +"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠢⠄⣀⣐⣠⣿⣃⡀⠉⠑⠚⠈⢧⡹⣄⠘⢧⠀⠈⢧⠀⠀⠀⠃⠀⠀⠎⠀⢀⡝⡰⣣⠏⠶⡚⠉⠁⠀⣧⣤⠐⣀⡠⠴⠒⠉⠁⠀⠀⠀⠀⠀⠀\n"
          +"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⠤⣤⣽⣮⡷⣌⣳⢤⡈⠁⣀⡀⠀⠀⣠⣠⠴⢋⣼⣯⣤⣤⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
          +"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⣷⣤⣴⣶⣦⣽⣷⣦⣴⣷⣶⣷⣶⣶⣖⣿⣧⣶⣿⣿⣿⣿⣿⣿⠁⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
          +"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠖⠚⠉⠉⠉⠁⠀⠉⠉⠉⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⡟⠛⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠉⠉⠁⠀⠀⠉⠉⠉⣽⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀\n"
          +"⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣭⣿⣿⣿⣿⣿⣿⣼⣿⣿⣿⣯⡽⠋⠁⠀⠀⠀⠀⣀⡄⠀⠀⠀⠀⣀⣤⣴⣷⣿⣧⡀⠀⠀⠀⠀⠀⠀\n"
          +"⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣵⣄⣀⣀⣠⣤⣾⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀\n"
          +"⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀\n"
          +"⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀\n"
          +"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠛⠻⠟⠻⠿⠿⠿⠿⠿⠿⠛⠛⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠛⠛⠛⠿⠿⠿⠟⠛⠛⠛⠛⠛⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀")
    print("Here is your peanut...", end =" ")