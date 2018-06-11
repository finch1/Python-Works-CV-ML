isRaining = False
isSunny = True

if isRaining and isSunny:
    print("We might see a rainbow")

if isRaining or isSunny:
    print("It might rain or sunshine")

if not isRaining:
    print("It must not be raining")

# list in python
ages = [12, 18, 39, 87, 7, 2]
for age in ages:
    isAdult = age > 17
    if not isAdult:
        print("Being " + str(age) + " doesn't make one an adult.")

# Looking for first mismatched letter
# A - Z -> 1-26
# first mismatch is between i and y, i.e. i = 9, y = 25,
# so 9 > 25 returns false
print("Jennifer" > "Jenny")

# len(x) takes one list as input and
# outputs whole number that represents the length of the list
print("Length of ages is: ", len(ages))
i = 0
for i in range(0, len(ages)):
    print("Index ", i, " holds ", ages[i])

print("sixaxis has %d number of characters" % len("sixaxis"))

# list of strings
names = ["tommy", "timmy","trip"]
i = 0
for i in range(0, len(names)):
    print(names[i], " has ", len(names[i]), " characters.")

# collections
candyCollection = {"bob" : 10, "mary" : 7, "sam" : 18}
candyCollection["bob"] = 22
print("Candy Collection with key and value has %d items inside it." % len(candyCollection))
for c in list(candyCollection):
    print(c, "has ", candyCollection.get(c), " candies.")
# range (x) takes one whole number as input - x
# and outputs a range instance that holds all the
# numbers counting by one between 0 and the input
numberedContestants = range(3)

# list(x) takes one input as tuple
# and outputs list containing same data as tuple

print("list func iterated contents of tuple: ", list(numberedContestants))

for c in list(numberedContestants):
    print("Contestant " + str(c))

for c in list(names):
    print(c)

# range(start, end, step)
numberedContestants = range(0, 10, 3)
print("Stepped list: ", list(numberedContestants))

# minimum and maximum
playerOneScore = 10
playerTwoScore = 4
print(min(playerOneScore, playerTwoScore))
print(min(0, 12, -19))

print(max("Kathryn", "Katie"))
print(min("Anny", "Bob"))

# round
print("Rounding 3.6 to ", round(3.6))
print("Rounding -3.6 to ", round(-3.6))

# abs(x) - input a whole or decimal number
# for positive input, same number is returned
# for negative input, positive is returned
print("ABS of 3.6: ", abs(3.6), ", 9: ", abs(9), ", -7: ", abs(-7), ", -0.1: ", abs(-0.1))

# sortinig function
print("Ages before sorting: ", list(ages))
print("Ages after sorting: ", sorted(ages))

# sorting with key params
alphabet = ['c','g', 'z', 't', 'H', 'P', 'A']
print("Alphabet before sorting: ", list(alphabet))
print("Ages after sorting: ", sorted(alphabet))
print("Ages after sorting with params: ", sorted(alphabet, key = str.lower))
sentence = "This is a string!"
print("Split a string: ", sentence.split())
sentenceList = sentence.split()
for c in range(0, len(sentenceList)):
    print(c, end=' ')

print()
sentenceList = sorted(sentence.split(), reverse = True, key = str.upper)
for c in list(sentenceList):
    print(c)

students = [('alice', 'G', 12), ('zelda', 'F', 32), ('therese', 'C', 34)]
print("Lambda Sort by name: ", sorted(students, key = lambda student:student[0]))
print("Lambda Sort by grade: ", sorted(students, key = lambda student:student[1]))

# type functions

class Car:
    pass

class Truck(Car):
    pass

c = Car()
t = Truck()
print("c is of type: ", type(c))
print("t is of type: ", type(t))

# is instance accounts for inheritance
print("Is Instance of = ", isinstance(c, Car))