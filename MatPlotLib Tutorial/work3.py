import matplotlib.pyplot as plt 
# scatter plot

x = range(1, 9)
y = [5,2,4,7,8,3,6,1]

plt.scatter(x, y, label = 'scat', color = 'k', marker = '+')

plt.show()