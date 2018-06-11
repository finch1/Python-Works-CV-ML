import numpy as nu 

# from list to numpy array
a = nu.arange(7)
print("Numpy array: ", a)
a = a-10+1
print("Numpy array tweaked: ", a)
print("Numpy array length: ", len(a))
print("Numpy array size: ", a.size)

# (start, stop, step)
a = nu.arange(10, 50, 10)
print("Numpy array, SSS: ", a)

# linspace()
a = nu.linspace(5, 15, 9)
print("Numpy linspace: ", a)

# zero() 3d, rows, col
a = nu.zeros([3,2,2])
a = a.astype(int)
print("Numpy zeros: \n", a)

# ones()
a = nu.ones([3,2,2])
a = a.astype(int)
print("Numpy ones: \n", a)
print("Numpy ones shape: ", a.shape)
print("Numpy ones number of dimentions: ", a.ndim)
print("Numpy ones number of elements: ", a.size)
print("Numpy ones number of length: ", len(a))
print("Numpy ones type of elements: ", a.dtype)
print("Numpy ones * 5 -1: \n", 5 * a -1)
a = a.reshape(4,3)
print("Numpy ones after reshape: \n", a)

# array shape()
a = nu.arange(1, 36)
print("Numpy array before shape: \n", a)
a.shape = (7,5)
print("Numpy array after shape: \n", a)
a.shape = (35)
print("Numpy as bool mask: \n", 0 == (a % 10))
sub_a = a[0 == (a % 10)]
print("Sub Array: \n", sub_a)

# array dot product
left_mat = nu.arange(6).reshape((2,3))
right_mat = nu.arange(15).reshape((3,5))
left_right_dot = nu.dot(left_mat, right_mat)
print("Dot of two matri: \n", left_right_dot)
print("Summ all elements: ", left_right_dot.sum())
print(nu.ones(35).astype(int).reshape((7,5))*3)

# creating structured arrays
# data definition array
person_data_def = [('name', 'S6'),('height','f8'),('weight','f8'),('age','i8')]
people_array = nu.zeros((4)).astype(person_data_def)
people_array[0] = ('Alfa', 65, 112, 23)
people_array[3] = ('Delta', 73, 205, 34)
# print info in the index zero through the last element, or 
# all elements within the array
print(people_array[0:])
# list only the ages
ages = people_array['age']
print(ages)