import os
import sys
import re

def main():
    freqWords = {}
    path = "./reviews/"
    
    for i in os.listdir(path):
        #print(i[-5])
        if (int(i[-5]) > 5):
            addFreqWords(i, freqWords, path)
        
    wordList = []
    for j in sorted(freqWords, key = freqWords.get, reverse = True):
        wordList.append(j)
    
    print("Top 100 Words Used in Positive Reviews\n"
          + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for k in range(0, 10):
        for l in range (0, 10):
            print(wordList[(k * 10) + l], end = "  ")
        print("")


def addFreqWords(fileName, freqWords, path):

    dontCareWords = ["this", "that", "take", "want", "which", "then", "than", 
                     "will", "with", "have", "after", "such", "when", "some", 
                     "them", "could", "make", "though", "from", "were", 'also', 
                     "into", "they", "their", "there", "because"]

    try:
        infile = open(path + fileName, "r")
    except FileNotFoundError:
        print("Failed to open file.")
        sys.exit()

    text = infile.read()
    infile.close()

    #text = ''.join(filter(whitelist.__contains__, text))
    text = re.sub("[^\sA-Za-z]","",text)
    text = text.lower()

    words = text.split()

    #print(words)
    #print()

    for i in list(words):
        if (i in dontCareWords or len(i) < 4):
            words.remove(i)

    for i in words:
        if (i in freqWords.keys()):
            freqWords[i] += 1
        else:
            freqWords[i] = 1
    print(freqWords)

main()