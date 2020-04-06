import numpy as np
import matplotlib.pyplot as plt
input_1 = (input('Nhập tọa độ x1, y1 = '))
x1, y1 = input_1.split(' ')
x1, y1 = (int(x1)), (int(y1))

#
input_2 = (input('Nhập tọa độ x2, y2 = '))
x2, y2 = input_2.split(' ')
x2, y2 = (int(x2)), (int(y2))

#
print('(x1, y1) = {}, {}'.format(x1, y1))
print('(x2, y2) = {}, {}'.format(x2, y2))
#
a = (y2 - y1) / (x2 - x1)
b = y1 - a*x1
#
plt.xlabel('X')
plt.ylabel('Y')
array_x = np.arange(-100, 100)
array_y = array_x * a + b
plt.plot(array_x, array_y)
plt.scatter([x1, x2],[y1, y2], color = 'red')

