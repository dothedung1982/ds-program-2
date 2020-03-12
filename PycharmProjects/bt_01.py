# Write a Python program to get the Python version you are using.
import sys

print("bt_01: Write a Python program to get the Python version you are using.=======")
print("Python version")
print(sys.version)
print("Version info.")
print(sys.version_info)

# list
my_list = [1, 2, 3, 4, 5]

# while Loop
print("====>> while Loop =======")
counter = 0
while counter < 5:
    print("counter is %d" % counter)
    counter = counter + 1

# for Loop
print("====>> for Loop =======")
counter = 0
for item in my_list:
    print("item[%d] is %d" % (counter, item))
    print("Total score for {0} is {1}".format(counter, item))
    print(f'Total score for {counter} is {item}.')
    counter = counter + 1


