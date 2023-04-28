import os

path = "/Users/aless/OneDrive/Desktop/Excercise2/Esercizio2"
counters = {}

filterFiles = []
for file in sorted(os.listdir(path)): #produce un elenco ordinato dei file all'interno della dir
    if file.endswith(".sh"):
        filterFiles.append(file) #aggiunge i file all'array filterFiles
        
        
def control(shebang_interpreter):
    t = []
    for word in shebang_interpreter:
        if word.startswith("-"): #nel caso in cui ci siano flag
            t.append(word)
        elif word.startswith("#!"):
            t.append(word)
        else:
            break;
    return " ".join(t)

     
for file in filterFiles:
    pathFile = os.path.join(path, file)
    if os.path.isfile(pathFile):
        with open(pathFile, 'r', encoding="iso-8859-1") as file:
            file_content = file.read()
            line_files_content = file_content.splitlines()
            shebang_interpreter  = line_files_content[0].split()
            if(len(shebang_interpreter) > 0 and shebang_interpreter[0].startswith("#!")):
                key = control(shebang_interpreter)
                if not key in counters: 
                    counters[key] = 0
                counters[key]+=1

print(counters)