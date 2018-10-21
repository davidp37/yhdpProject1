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


#search("..", ".txt")


