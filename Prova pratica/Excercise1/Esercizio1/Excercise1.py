import os
import sys

if len(sys.argv) != 4:
    print("Arguments must be 3")
    print(sys.argv[1])
    sys.exit()
# Leggi i parametri dalla riga di comando
startPath = sys.argv[1]
wordToReplace = sys.argv[2]
valueWord = sys.argv[3]

if not os.path.isdir(startPath):
    print("Insert a valid path")
    sys.exit()

def changeOccuranceFiles(path = startPath):
    files = os.listdir(path)
    for file in files:
        pathFile = os.path.join(path, file)
        if os.path.isdir(pathFile):
            changeOccuranceFiles(pathFile)
        if os.path.isfile(pathFile):
            with open(pathFile, 'r', encoding="iso-8859-1") as file:
                file_content = file.read()
            new_content = file_content.replace(wordToReplace, valueWord)
            with open(pathFile, 'w') as file:
                file.write(new_content)

changeOccuranceFiles()
print("Done!")