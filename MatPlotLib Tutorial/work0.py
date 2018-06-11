import matplotlib.pyplot as plt

# linear plot

x1 = [1,2,3]
y1 = [6,5,4]

x2 = [6,5,4]
y2 = [1,2,3]

plt.plot(x1, y1, label='First Line')
plt.plot(x2, y2, label='Second Line')
plt.legend()
plt.show()