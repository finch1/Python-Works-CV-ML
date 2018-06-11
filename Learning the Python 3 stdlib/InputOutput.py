import sys

# print Arguments
print("Number of arguments: ", len(sys.argv))
print("Arguments ", sys.argv)

# remove arguments
sys.argv.remove(sys.argv[0])

print("Arguments ", sys.argv)
arguments = sys.argv
# sum the args
sum = 0
for arg in arguments:
    try:
        sum = sum + int(arg)
    except Exception:
        print("Bad input")

print("Sum of arguments: ", sum)

# input
color = input("Qual est tu favourite color?\n")
print("Your choice is: ", color)

# files and file writing
# open a file
myFile = open("scores.txt", "w")
# show attributes and properties of that file
print("Name " + myFile.name)
print("Mode " + myFile.mode)
# erase whatever is in the file and write new
myFile.write("GBJ : 100\nKHD : 99\nBBB : 89")
myFile.close()
# read the file, seek pointer, read again
myFile = open("scores.txt", "r")
print("Mode " + myFile.mode)
conents = myFile.read()
print(conents)
myFile.seek(11)
conents = myFile.read()
print(conents)
myFile.close()

# iterative files
myFile = open("scores.txt", "r")

# read one line at a time
print("One line from the file: " + myFile.readline())
myFile.seek(0)

# iterate through each line of a file
for line in myFile:
    newHighScorer = line.replace("BBB", "PDJ")
    print(newHighScorer)

myFile.close()
