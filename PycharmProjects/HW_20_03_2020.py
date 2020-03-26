# 1.	List comprehension
# a.	Generate a list as follows: x = [0.1,0.2,0.3, …., 4.9, 5.0]
print("a.	Generate a list as follows: x = [0.1,0.2,0.3, …., 4.9, 5.0]")
x = [x / 10 for x in range(1, 51)]
print (x)

# b.	Compute the value of function f(x) = 2 * cos(x)
import math
f_x = [2 * math.cos(e) for e in x]
print(f_x)

#c.	Plot function f(x) using mathplotlib
import matplotlib.pyplot as plt
fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot(x, f_x)  # Plot some data on the axes.