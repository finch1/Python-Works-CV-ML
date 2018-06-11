import math
import random as rd
import statistics as st
import itertools as itt

# constants
print("Pi ", math.pi, ", e ", math.e)

# trigonometry
obst_direction = math.cos(math.pi / 4)
print("Obstacle direction: ", obst_direction)

# Ceil & Floor 
cookies = 10.3
candy = 7
print("Ceil ", math.ceil(cookies))
print("Floor ", math.floor(candy))

# factorial and square root
print("Square Root ", math.sqrt(25))
print("Factorial ", math.factorial(5))

# GCD
print("GCD : ", math.gcd(8, 52))

# degree & radians
print("How many radiance are in a full circle or 360D: ", math.radians(360))
print("How many radiance are in a full circle or 360D: ", math.pi*2)
print("How many degrees are in a full circle or 2Pi: ", math.degrees(math.pi*2))

# random(exclusive value)
decider = rd.randrange(2)
if decider == 0:
    print("Heads")
else:
    print("Tails")

# random(inclusive value, exclusive value)
print("You rolled a " + str(rd.randrange(1, 7))) 

# random choices
lotteryWinner = rd.sample(range(100), 5)
print("Lottery Winners:", lotteryWinner)

possibleNames = ["Alex", "Bit", "Cody", "Dex"]
print("Possible name: ", rd.choice(possibleNames))
rd.shuffle(possibleNames)
print("Shuffled names: ", possibleNames)

# statistics
ages = rd.sample(range(10, 30), 10)

for i in (list(ages) * 5):
    ages.append(rd.randrange(10, 30))

print("Age mean ", st.mean(ages))
#print("Age mode ", st.mode(ages))
print("Age median ", st.median(ages))

# variance - the average of the squared differences from the mean
print("Variance: ", st.variance(ages))
# standard deviation - the square root of the variance
print("Variance: ", st.stdev(ages))

print("Ages sorted : ", sorted(ages))

# infinite counting
for x in itt.count(50, 5):
    print(x)
    if x == 80:
        break

for x in itt.cycle("RACECAR."):
    print(x)
    if x == '.':
        break

# Permutations: order matter - some copies with same inputs
# but in different order
election = {1: "Barb", 2:"Karen", 3:"Erin"}
for p in itt.permutations(election):
    print(p)

for p in itt.permutations(election.values()):
    print(p)

# combinations: Order does not matter - no copies with same input
colorsForPainting = ["Red", "Blue", "Purple", "Orange", "Yellow", "Pink"]

for c in itt.combinations(colorsForPainting, 2):
    print(c)
