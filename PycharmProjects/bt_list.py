# https://www.w3schools.com/python/python_lists.asp
# Khai bao list
my_list = ["Hello", 11, 22]

# ===== Copy sang 1 bien moi va phan phat dia cho cung nho moi
print('---> Copy sang 1 bien moi va phan phat dia cho vung nho moi')
my_list_1 = my_list[:]
print(my_list_1)
my_list_1[0] = 'World'
print(my_list)  # --> my_list khong bi thay doi data

# ===== Copy sang 1 bien moi cùng dia chi vung nho
print('---> Copy sang 1 bien moi cùng dia chi vung nho')
my_list_2 = my_list
print(my_list_2)
my_list_2[0] = 'World'
print(my_list)  # --> my_list[0] bi doi theo

# Access Items
print('---> Access Items')
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Negative Indexing
print('---> Negative Indexing')
print(thislist[-1])
print(thislist[-2])

# Range of Indexes
print('---> Range of Indexes')
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# Copy a List
print('---> Copy a List')
mylist = thislist.copy()
print(mylist)

# Join Two Lists
print('---> Join Two Lists')
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# Join Two Lists
print('---> Remove các element ko phải là int')
l1 = ['aaa', 2, 'bb', 13.5, 10, ['aaa', 11]]
list2 = []
for e in l1:
    if type(e) == str:
        list2.append(e)
list3 = []
for e in l1:
    if (e in list2) == 0:
        list3.append(e)
print(list3)












