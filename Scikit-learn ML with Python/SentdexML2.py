import matplotlib.pyplot as plt
import numpy as np

from sklearn import datasets #import load_digits
from sklearn import svm # support vector machine

digits = datasets.load_digits()
# myFile = open("data.txt", "w")
# myFile.write(digits.data)
# myFile.clsoe()
#print(digits.data)
# print(digits.target)
# print(digits.images[0])

#setup classifier

# clf = svm.SVC(gamma = 0.001, C=100)

# print(len(digits.data))

# x,y = digits.data[:-1], digits.target[:-1]
# clf.fit(x,y)

# print('Prediction:', clf.predict(digits.data[-1]))

# plt.imshow(digits.images[-1], cmap=plt.cm.gray_r, interpolation="nearest")
# plt.show()