import re
import os

def searchINFiles(folder_path,regex):
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path=os.path.join(folder_path,filename)
            with open(file_path,'r') as file:
                print('serching in %s...',%filename)
                for numline,line in enumerate(file,start=1):
                    if re.search(regex):
                        print('found at line %s:%s',(%numline,%line))
folderPath=input('enter the folder path')
userregex=input('enter the regex pattern.')

searchINFiles(folderPath,userregex)