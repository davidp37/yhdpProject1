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


# Takes user input to determine what actions to perform


def start():
    command = input ("Enter a command: ")
    command = command.split()
    choice = command[0]
    file = command[1]
    loop = True
    while(loop):
        switcher = {
            '''
            "D": fileTaker_D(file),
            "R": fileTaker_R(file),
            "A": fileTaker_A(file),
            "N": fileTaker_N(file),
            "E": fileTaker_E(file),
            "T": fileTaker_T(file),
            "<": fileTaker_<(file),
            ">": fileTaker_>(file),
            '''
            "test": print("123"),
            "T": def temp():
                fileTaker_Test(file)
    }
        print(choice)
        func = switcher.get(choice, lambda: "Error")
        loop = False

def fileTaker_Test(file = ""):
    print("test")



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


def copy(files = []):
    for name in files:
        print(name)
        print(str(name)[:len(str(name))-len(type)])
        copy =  (str(name)[:len(str(name))-len(type)]) + ".dup" + type
        shutil.copy(name, copy)

# Prints the first line of each file of a given array


def printLine(files=[]):
    for file in files:
        current = open(file, "r")

        if not str(file)[-4:] == ".txt":
            print("NOT TEXT")
        else:
            file.readline()
        current.close()

# Touches each file of a given array, changing its timestamp to the current time


def touch(files = []):
    for file in files:
        os.utime(file)


# Starts program

start()






#search("..", ".txt")


