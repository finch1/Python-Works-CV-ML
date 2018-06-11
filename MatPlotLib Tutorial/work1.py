import matplotlib.pyplot as plt 
# bar chart 

x1 = [2, 4, 6, 8, 10]
y1 = [6, 7, 8, 2, 4]

x2 = [1, 3, 5, 7, 9]
y2 = [7, 4, 5, 3, 9]

plt.bar(x1, y1, label = 'Bars1', color='magenta')
plt.bar(x2, y2, label = 'Bars2', color='cyan')
plt.legend()
plt.show()
