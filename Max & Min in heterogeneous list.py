#Max/Min in heterogeneous list
list1 = ['hello', 12, 23, 5, 7, 'python', 8, 3]
temp = 0
j = 0
k = 0
for i in list1:
    if (type(i) == type(3)):
        if j < i:
            j = i
        if temp == 0:
            k = i
            temp += 1
        if k > i:
            k = i

print("maximum value of the list:", j)
print("minimum value of the list:", k)
