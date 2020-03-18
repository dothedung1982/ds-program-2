# đếm xem có bao nhiêu từ đơn
print('--> đếm xem có bao nhiêu từ đơn')
s = 'You can loop through the list items by using a for loop:'
n = len(s.split())
print(n)

# chỉ để lại 1 khoảng trắng
print('--> chỉ để lại 1 khoảng trắng giữa các ký tự')
s = 'You   can loop    through the   list items   by   using a for   loop:'
n = ' '.join(s.split())
print(n)

print('--> đếm số lần xuất hiện giữa các ký tự Cách 1')
s1 = 'You   can loop    through the   list items   by   using a for   loop:'
se1 = set(s)
se2 = {}
for e in se1:
    se2[e] = s1.count(e)
print(se2)

print('--> đếm số lần xuất hiện giữa các ký tự Cách 2')
#se3 = {}
#for e in se1:
    #se3[e] = se3[e] + 1 if
#print(se2)

l1 = ['aaa', 2, 'bb', 13.5, 10]
list2 = []
for e in l1:
    if type(e) == str:
        list2.append(e)
print(list2)





