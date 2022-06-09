#Armstrong Number
a= int(input("Enter a number:"))
b= len(str(a))
print(b)
j=0
temp=a
while(temp>0):
     i=int(temp%10)
     j=int((i**b)+j)
     temp=int(temp/10)
if j==a:
    print(a, "is an armstrong number")
else:
    print(a, "is not an armstrong number")
