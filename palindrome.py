#palindrome number
a=int(input("Enter a number:"))
j=0
temp=a
while(temp>0):
    i=(int(temp%10))
    j= int(j*10+i)
    temp= int(temp/10)

if a==j:
    print(a,"is a palindrome number")
else:
    print(a, "is not a palindrome number")
