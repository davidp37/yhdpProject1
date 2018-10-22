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
- T : text files that contain a given textr
- < : files whose sizes

"""
global start
start = os.path.abspath('.')

if '/' in start:
    start = start[:start.find('/')]
if "\\" in start:
    start = start[:start.find('\\')]


# Takes user input to determine what actions to perform


def start():

    '''
    loop = True
    while(loop):
        switcher = {
            
            "D": fileTaker_D(file),
            "R": fileTaker_R(file),
            "A": fileTaker_A(file),
            "N": fileTaker_N(file),
            "E": fileTaker_E(file),
            "T": fileTaker_T(file),
            "<": fileTaker_<(file),
            ">": fileTaker_>(file),
        }
        print(choice)
        func = switcher.get(choice)
        func("threui")
        loop = False
        '''
    loop = True
    while loop:
        command = input("Enter a command: ")
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
        if file == "":
            print("ERROR")
            loop = True
        elif choice == "D":
            names = interesfileTaker_D(file)
        elif choice == "R":
            names = fileTaker_R(file)
        else:
            print("ERROR");
            loop = True
        for entry in names:
            print(os.path.abspath(entry))
        step2(names)

# Takes the second input from the user to decide which of the files to mark as interesting


def step2(names):
    loop = True
    while loop:
        command = input("Enter a command: ")
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
        except ValueError:
            print("Error")
            loop = True
        else:
            print("ERROR");
            loop = True

        for entry in interesting:
            print(os.path.abspath(entry))
        step3(interesting)


# Takes the third input from the user to decide what to do with the interesting files


def step3(names):
    loop = True
    if len(names)==0:
        loop = False
    while loop:
        loop = False
        command = input("Enter a command: ")
        command = command.split()
        choice = ""
        file = ""
        try:
            choice = command[0]
            file = command[1]
        except IndexError:
            print("")
        if file == "":
            print("ERROR")
            loop = True
        elif choice == "F":
            copy(names)
        elif choice == "D":
            printLine(names)
        elif choice == "T":
            touch(names)
        else:
            print("ERROR")
            loop = True


''' Takes a list of files and an integer, and returns only the files 
    in the list that are smaller than the given integer in bytes '''


def fileTaker_Less(names, size):
    for i in range(len(names), 0, -1):
        if not os.stat(names[i]).st_size <= size:
            names.remove(i)
    return names


''' Takes a list of files and an integer, and returns only the files 
    in the list that are Larger than the given integer in bytes '''


def fileTaker_Greater(names, size):
    for i in range(len(names), 0, -1):
        if not os.stat(names[i]).st_size >= size:
            names.remove(i)
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


# Starts program

start()


#search("..", ".txt")
