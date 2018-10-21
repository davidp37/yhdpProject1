from pathlib import Path
import os

"""
fileTaker_D
	all of the files in that directory will be under consideration, 
	but no subdirectories (and no files in those subdirectories) will be.
"""
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


"""
fileTaker_R
	all of the files in that directory will be under consideration, 
	along with all of the files in its subdirectories, all of the files in their subdirectories, 
	and so on. (You can think of the letter R here as standing for "recursive.")
"""
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

"""
sortPaths
	Takes List object for an paramaeter, and sorts everything in it in lexicographical order
	Returns the sorted list
"""
def sortPaths(lis: list):
	return sorted(lis, key=lambda p: (os.path.dirname(p), os.path.basename(p)))


"""
printPaths
	takes List object for an paramaeter, and prints out everything in the list of Path objects
"""
def printPaths(lis: list):
	for name in lis:
		print(name)

"""
main for Test
"""
# First, Take the input
line = input()
# Read the first line = Letter (D or R) + path to directory
# otherwise print ERROR
LetterAndPath = line.split()
path = Path(os.path.abspath(LetterAndPath[1]))

myList = []
if LetterAndPath[0] == 'D':
	print("Operation Type: D")
	myList = fileTaker_D(path)
elif LetterAndPath[0] == 'R':
	print("Operation Type: R")
	fileTaker_R(path, myList)
else:
	print("ERROR: ", "\n")

# make sure the path is stored as Path obj, not string
print("\nIn myList (type: ", type(myList[0]), ")...\n")	

# Next, the program prints the paths to every file that is under consideration
printPaths(sortPaths(myList))

# Read another line of input = Search Characteristics Letter (A, N, E, T, <, >)
# otherwise print ERROR

# Nect, Print the paths to every file that is considered interesting, based on the search characteristic.
# If there were no interesting files, the program ends; there is no action to take.

# Reads a line of input = Action that will be taken on each interesting file (F, D, T)
# otherwise print ERROR

# Once an action has been taken on each file, the program ends.