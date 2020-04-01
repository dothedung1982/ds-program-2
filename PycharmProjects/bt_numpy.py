import numpy as np
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
b = np.array(range(1, 10))
print('a = ',a)
print('b = ',b)
#
import cv2
img = cv2.imread('IMG_6426.PNG')
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

