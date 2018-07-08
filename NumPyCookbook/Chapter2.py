import scipy.misc
import numpy as np 
import matplotlib.pyplot as plt 

LENA_X = 768
LENA_Y = 1024
LENA_Z = 3

lenna = scipy.misc.face()
print(lenna[0, :2])


# check the array (image) shape - optinoal sanity check
np.testing.assert_equal((LENA_X, LENA_Y, LENA_Z), lenna.shape)

xfactor = 2
yfactor = 2

# resize the array eith repeat(). We give this function a resize
# factor in the x and y directions
resized = lenna.repeat(yfactor, axis=0).repeat(xfactor, axis=1)

# check resize shape
np.testing.assert_equal((LENA_X * xfactor, LENA_Y * yfactor, LENA_Z), lenna.shape)

print(resized.shape)
print(resized[0, :4])

plt.subplot(121)
plt.imshow(lenna)
plt.title("Org")

plt.subplot(122)
plt.imshow(resized)
plt.title("Rsz")

plt.show()

