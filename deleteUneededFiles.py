import os

def delUneededFiles(folder):
    for folderName,SubFolders,fileNames in os.walk(folder):
        print(folderName)
        for subfolder in SubFolders:
            if os.path.getsize(subfolder) > 1:
                print(os.path.abspath(subfolder))
                print(subfolder)
        for filename in fileNames:
            if os.path.getsize(filename) > 1:
                print(os.path.abspath(filename))
                print(filename)

folder='../Downloads'
delUneededFiles(folder)

        