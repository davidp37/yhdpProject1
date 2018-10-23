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
global start
start = os.path.abspath('.')

if '/' in start:
    start = start[:start.find('/')]
if "\\" in start:
    start = start[:start.find('\\')]


# fileTaker_D: Returns List object with ONLY files in that directory 


def fileTaker_D(path: Path):
    fileList = []
    try:
        for file in os.listdir(path):
            if os.path.exists(file) and os.path.isfile(file):
                # print(os.path.abspath(file))
                fileList.append(Path(os.path.abspath(file)))
    except Exception as exceptObj:
        print("ERROR: ", str(exceptObj))
    return fileList


# fileTaker_R: Returns List object with files in this directory and subdirectories


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


def sortPaths(lis: list):
    std = sorted(lis, key=lambda p: (os.path.dirname(p), os.path.basename(p))).copy()
    return std



# printPaths: Prints out everything in the list


def printPaths(lis: list):
    for name in lis:
        print(name)


# fileTaker_A: all of the files found in the previous step are considered interesting
# Not sure if even need this


def fileTaker_A(names: list):
    return names


# fileTaker_N: returns List object with the Paths to the file whose name exactly match "file"


def fileTaker_N(names: list, file: str):
    lis = []
    for p in names:
        if os.path.basename(p) == file:
            lis.append(p)
    return lis


# fileTaker_E: returns List object with Paths to files whose has an extention specified in "file"


def fileTaker_E(names: list, file: str):
    lis = []
    for p in names:
        root, ext = os.path.splitext(os.path.basename(p))
        if ext == file or ext == "." + file:
            lis.append(p)
    return lis

    
# fileTaker_T: returns List object of text files which contains strings specified by "file"


def fileTaker_T(names: [list], file: str)-> list:
    lis = []
    origin = os.getcwd()
    for p in names:
        found = False
        if os.path.exists(p) and os.path.dirname(p) != os.getcwd():
            os.chdir(os.path.dirname(p))
        try:
            infile = open(os.path.basename(p), "r", encoding="ISO-8859-1")

            if file in infile.read():
                # string in "file" found in the text file
                lis.append(p)
                found = True
        except Exception as exceptObj:
            print("ERROR: ", str(exceptObj), " is not a text file.")
        infile.close()
    return lis


''' Takes a list of files and an integer, and returns only the files 
    in the list that are smaller than the given integer in bytes '''


def fileTaker_Less(names, size):
    for i in range(len(names)-1, -1, -1):
        if os.stat(names[i]).st_size > int(size):
            del names[i]
    return names


''' Takes a list of files and an integer, and returns only the files 
    in the list that are Larger than the given integer in bytes '''


def fileTaker_Greater(names, size):
    for i in range(len(names)-1, -1, -1):
        if os.stat(names[i]).st_size < int(size):
            del names[i]
    return names




# Copies all files for a given file type in a given directory


def copyDirect(direct, type):
    names = []
    for file in os.listdir(direct):
        try:
            names = glob.glob('*'+type)
        except IOError:
            print("error")
    if not os.path.isdir(os.path.join(direct, "COPIES")):
        os.mkdir(os.path.join(direct, "COPIES"))
    for name in names:
        print(name)
        print(str(name)[:len(str(name))-len(type)])
        dest =  (str(name)[:len(str(name))-len(type)]) + ".dup" + type
        shutil.copy(name, dest)

# Copies all files in a given array


def copy(files):
    for name in files:
        print(name)
        print(str(name)[:len(str(name))-len(type)])
        copy =  (str(name)[:len(str(name))-len(type)]) + ".dup" + type
        shutil.copy(name, copy)

# Prints the first line of each file of a given array


def printLine(files):
    for file in files:
        current = open(file, "r")

        if not str(file)[-4:] == ".txt":
            print("NOT TEXT")
        else:
            file.readline()
        current.close()

# Touches each file of a given array, changing its timestamp to the current time


def touch(files):
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


def step2(names):
    loop = True
    while loop:
        command = input("Enter a command (step 2): ")
        command = command.split()
        choice = ""
        file = ""
        interesting = []

        try:
            choice = command[0]
            file = command[1]
        except IndexError:
            print("")
        if choice == "T":
            file = ' '.join(command[1:])
        loop = False
        try:
            if choice == "A" and file == "":
                interesting = fileTaker_A(names)
            elif choice == "N" and not file == "":
                interesting = fileTaker_N(names, file)
            elif choice == "E" and not file == "":
                interesting = fileTaker_E(names, file)
            elif choice == "T":
                interesting = fileTaker_T(names, file)
            elif choice == "<" and int(file) >= 0:
                interesting = fileTaker_Less(names, file)
            elif choice == ">" and int(file) >= 0:
                interesting = fileTaker_Greater(names, file)
            else:
                print("ERROR")
                loop = True
        except ValueError as e:
            print("Error" + str(e))
            loop = True
    printPaths(interesting)
    step3(interesting)


# Takes the third input from the user to decide what to do with the interesting files


def step3(names):
    loop = True
    while loop:
        loop = False
        choice = input("Enter a command (step 3): ")
        if choice == "F":
            copy(names)
        elif choice == "D":
            printLine(names)
        elif choice == "T":
            touch(names)
        else:
            print("ERROR")
            loop = True


# Starts program

start()
