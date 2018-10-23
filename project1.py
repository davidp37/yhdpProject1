import os
from pathlib import Path
import os.path
import glob
import shutil

"""
General Notes:

- Should not prompt user, just read input
- Store paths as objects
- Be error proof, skip files if there is an error with them
- written entirely in 1 file
- try to make complex functions into several smaller ones
- D : files that are in this directory ONLY
- R : files in this directory and ALL SUBDIRECTORIES
- Wrong format or no directory: Print ERROR
- A : all files are interesting
- N : search for only a particular name(with extension)
- E : search for all files with a particular extension
- T : text files that contain a given text
- < : files whose sizes

"""

# fileTaker_D: Returns List object with ONLY files in that directory

def fileTaker_D(path: Path)-> list:
    fileList = []
    try:
        for file in os.listdir(path):
            if os.path.exists(file) and os.path.isfile(file):
                # print(os.path.abspath(file))
                fileList.append(Path(os.path.abspath(file)))
    except Exception as exceptObj:
        print("ERROR: ", str(exceptObj))
    return fileList


# fileTaker_R: Recieves Path and list object and adds files in this directory and subdirectories to the given list
# This function returns nothing.

def fileTaker_R(path: Path, fileList: list):
    if os.path.exists(path) and path != os.getcwd():
        os.chdir(path)
    for name in os.listdir(path):
        try:
            if os.path.exists(name):
                if os.path.isfile(name):
                    # print(os.path.abspath(name))
                    fileList.append(Path(os.path.abspath(name)))
                elif os.path.isdir(name):
                    fileTaker_R(Path(os.path.abspath(name)), fileList)
        except Exception as exceptObj:
            print("ERROR: ", str(exceptObj))
    os.chdir("..")


# sortPaths: sorts everything in the lis in lexicographical order and returns the sorted list


def sortPaths(_list: list)-> list:
    std = sorted(_list, key=lambda p: (os.path.dirname(p), os.path.basename(p))).copy()
    return std



# printPaths: Prints out everything in the list


def printPaths(_list: list):
    for name in _list:
        print(name)


# fileTaker_A: all of the files found in the previous step are considered interesting
# Not sure if even need this


def fileTaker_A(names: list)->list:
    return names


# fileTaker_N: returns List object with the Paths to the file whose name exactly match "file"


def fileTaker_N(names: list, file: str)->list:
    _list = []
    for p in names:
        if os.path.basename(p) == file:
            _list.append(p)
    return _list


# fileTaker_E: returns List object with Paths to files whose has an extention specified in "file"


def fileTaker_E(names: list, file: str)->list:
    _list = []
    for p in names:
        root, ext = os.path.splitext(os.path.basename(p))
        if ext == file or ext == "." + file:
            _list.append(p)
    return _list

    
# fileTaker_T: returns List object of text files which contains strings specified by "file"


def fileTaker_T(names: [list], file: str)-> list:
    _list = []
    origin = os.getcwd()
    for p in names:
        found = False
        if os.path.exists(p) and os.path.dirname(p) != os.getcwd():
            os.chdir(os.path.dirname(p))
        try:
            infile = open(os.path.basename(p), "r", encoding="ISO-8859-1")
            if file in infile.read():
                # string in "file" found in the text file
                _list.append(p)
                found = True
        except Exception as exceptObj:
            print("ERROR: ", str(exceptObj), " is not a text file.")
        infile.close()
    return _list


''' Takes a list of files and an integer, and returns only the files 
    in the list that are smaller than the given integer in bytes '''


def fileTaker_Less(names: list, size: int)->list:
    for i in range(len(names)-1, -1, -1):
        if os.stat(names[i]).st_size > int(size):
            del names[i]
    return names


''' Takes a list of files and an integer, and returns only the files 
    in the list that are Larger than the given integer in bytes '''


def fileTaker_Greater(names: list, size: int)->list:
    for i in range(len(names)-1, -1, -1):
        if os.stat(names[i]).st_size < int(size):
            del names[i]
    return names


 # Copies all files in a given array


def copy(files: list):
    for name in files:
        ext = 0
        for i in range(0,len(str(name))-1):
            if str(name)[-i] == ".":
                ext = (-i)
                break
        type = str(name)[ext:]
        copy = (str(name)[:len(str(name))+ext]) + ".dup" + type
        shutil.copy(name, copy)

# Prints the first line of each file of a given array


def printLine(files: list):
    for file in files:
        current = open(os.path.basename(file), "r")
        try:
            for line in current:
                print(line)
                break
        except Exception as e:
            print("NOT TEXT " + str(e))
        current.close()

# Touches each file of a given array, changing its timestamp to the current time


def touch(files: list):
    for file in files:
        os.utime(file)


# Takes user input to determine what actions to perform


def start():

    loop = True
    while loop:
        command = input("Enter a command (start): ")
        command = command.split()
        choice = ""
        file = ""
        names = []
        try:
            choice = command[0]
            file = command[1]
        except IndexError:
            print("")
        loop = False
        path = os.path.abspath(file)
        if file == "":
            print("ERROR")
            loop = True
        elif choice == "D" and os.path.exists(path):
            names = fileTaker_D(path)
            names = sortPaths(names)
            printPaths(names)
        elif choice == "R" and os.path.exists(path):
            fileTaker_R(path, names)
            names = sortPaths(names)
            printPaths(names)
        else:
            print("ERROR")
            loop = True
    step2(names)

# Takes the second input from the user to decide which of the files to mark as interesting


def step2(names: list):
    loop = True
    while loop:
        command = input("Enter a command (step 2): ")
        command = command.split()
        choice = ""
        choice2 = ""
        interesting = []

        try:
            choice = command[0]
            choice2 = command[1]
        except IndexError:
            print("")
        if choice == "T":
            choice2 = ' '.join(command[1:])
        loop = False
        try:
            if choice == "A" and choice2 == "":
                interesting = fileTaker_A(names)
            elif choice == "N" and not choice2 == "":
                interesting = fileTaker_N(names, choice2)
            elif choice == "E" and not choice2 == "":
                interesting = fileTaker_E(names, choice2)
            elif choice == "T" and not choice2 == "":
                interesting = fileTaker_T(names, choice2)
            elif choice == "<" and int(choice2) >= 0:
                interesting = fileTaker_Less(names, choice2)
            elif choice == ">" and int(choice2) >= 0:
                interesting = fileTaker_Greater(names, choice2)
            else:
                print("ERROR")
                loop = True
        except ValueError as e:
            print("Error" + str(e))
            loop = True
    printPaths(interesting)
    step3(interesting)


# Takes the third input from the user to decide what to do with the interesting files


def step3(names: list):
    loop = True
    while loop:
        loop = False
        choice = input("Enter a command (step 3): ")
        if choice == "F":
            printLine(names)
        elif choice == "D":
            copy(names)
        elif choice == "T":
            touch(names)
        else:
            print("ERROR")
            loop = True


# Starts program

start()
