import os

fileName = "bd.log"


def updateLogFile(fileName) :

    tempFileName = fileName[0:fileName.index(".log")] + '.temp'

    with open(fileName) as f :
        f = f.readlines()

    with open(tempFileName,'w') as file_tem :
        for line in f :
            for phrase in ["A complete LUP transaction"]:
                if phrase in line:
                    y=line.index("'msisdn': '")
                    phoneReplaced = line.replace(line[y+11:y+22], '00')
                    file_tem.write(phoneReplaced)
                else :
                    file_tem.write(line)


    fileExtension = fileName[fileName.index("log"):len(fileName)]
    newNameFile = tempFileName.replace('temp',fileExtension)
    os.remove(fileName)
    os.rename(tempFileName,newNameFile)



updateLogFile(fileName)