from genericpath import isfile
from operator import truediv
import os
import sys

#Ex 1
def extensions(dir_path):
    lines=[]
    for line in os.scandir(dir_path):
        if line.is_file(): 
            extension = os.path.splitext(dir_path + line.name)
            lines.append(extension[1])
    list.sort(lines,key=lambda x: x[1])
    return lines

# print(extensions("C:/Users/Moraru George/Desktop/Python"))

#Ex 2
def writeInFile(dir_path, file_path):
    file = open(file_path,"wt")
    for line in os.scandir(dir_path):
        if line.is_file() and line.name[0] == 'A':
            file.write(line.path+'\n')
    file.close()
    return 1

# writeInFile("C:/Users/Moraru George/Desktop/Python","C:/Users/Moraru George/Desktop/Python/Fisier.txt")

#Ex 3
def findAllExtensions(my_path):
    lines = []
    for line in os.scandir(my_path):
        if line.is_file():
            extension = os.path.splitext(line.path)
            if extension[1] != '':
                lines.append(extension[1])
        elif line.is_dir():
            lines.extend(findAllExtensions(line.path))
    return lines

def dirProceed(my_path):
    lines = findAllExtensions(my_path)
    tuples = []
    for line in lines:
        if (line,lines.count(line)) not in tuples:
            tupleToAdd = (line, lines.count(line))
            tuples.append(tupleToAdd)
    tuples.sort(key=lambda x: x[1],reverse=True)
    return tuples

def fileProceed(my_path):
    file = open(my_path,'r')
    str_array = ''
    for line in file.readlines():
        str_array = str_array + line
    string = str_array[-20:] if len(str_array) >= 20 else str_array
    return string

def fileOrDir(my_path):
    result = fileProceed(my_path) if os.path.isfile(my_path) else dirProceed(my_path)
    return result 

# print(fileOrDir("C:/Users/Moraru George/Desktop/Python"))
# print(fileOrDir("C:/Users/Moraru George/Desktop/Python/Abc.txt"))

#Ex 4
def inputFile():
    if len(sys.argv)>1:
        dir_path = sys.argv[1]
        print(dir_path)
        if os.path.isfile(dir_path):
            print("You have entered a file path. Please try again!")
            inputFile()
            exit(0)
        extensionArray = extensions(dir_path)
        extensionArray = sorted(set(extensionArray))
        print('These are the unique extensions: ')
        print(extensionArray)
    else:
        print("No argument given! Exit.")
        exit(0)

inputFile()

#Ex 5
def stringInFile(target, to_search):
    file = open(target, 'r', encoding='latin-1')
    for line in file.readlines():
        if to_search in line:
            file.close()
            return True
    file.close()
    return False

def stringToSearch(target, to_search):
    try:
        assert (os.path.isfile(target) or os.path.isdir(target)), "The path is nor a file or a directory!"
    except Exception as e:
        raise ValueError(e)
    else:
        files = []
        if os.path.isfile(target) and stringInFile(os.path.abspath(target),to_search):
            files.append(os.path.basename(target))
        elif os.path.isdir(target):
            for line in os.scandir(target):
                if line.is_file() and stringInFile(line.path,to_search):
                    files.append(line.name)
                elif line.is_dir():
                    files.extend(stringToSearch(line.path,to_search))
        return files
        
# print(stringToSearch("C:/Users/Moraru George/Desktop/Pytho", "Ipsum"))


#Ex 6
def printException(e):
    print(e)

def stringToSearchCallBack(target, to_search, callbackFunction):
    try:
        assert (os.path.isfile(target) or os.path.isdir(target)), "The path is nor a file or a directory!"
        files = []
        if os.path.isfile(target) and stringInFile(os.path.abspath(target),to_search):
            files.append(os.path.basename(target))
        elif os.path.isdir(target):
            for line in os.scandir(target):
                if line.is_file() and stringInFile(line.path,to_search):
                    files.append(line.name)
                elif line.is_dir():
                    files.extend(stringToSearchCallBack(line.path,to_search,printException))
        return files
    except Exception as e:
        callbackFunction(e)
        raise SystemExit
    
# print(stringToSearchCallBack("C:/Users/Moraru George/Desktop/Pytho","Ipsum",printException))

#Ex 7
def fileProperties(file_path):
    try:
        dictionary = dict()
        with open(file_path, 'r') as file:
            dictionary['full_path'] = os.path.abspath(file_path)
            dictionary['file_size'] = str(os.path.getsize(file_path)) + ' B'
            dictionary['file_extension'] = os.path.splitext(file_path)[1] if os.path.splitext(file_path)[1] != '' else ''
            dictionary['can_read'] = os.access(file_path,os.R_OK)
            dictionary['can_write'] = os.access(file_path, os.W_OK)
            file.close()
        return dictionary
    except FileNotFoundError as e:
        print(e)
        raise SystemExit

# print(fileProperties("C:/Users/Moraru George/Desktop/Python/Abcd.txt"))

#Ex 8
def absoluteFilePaths(dir_path):
    try:
        files = []
        assert os.path.isdir(dir_path), 'This path is not a directory!'
        for line in os.scandir(dir_path):
            if os.path.isfile(line.path):
                files.append(os.path.abspath(line.path))
        return files
    except Exception as e:
        raise ValueError(e)

# print(absoluteFilePaths("C:/Users/Moraru George/Desktop/Python"))
        
