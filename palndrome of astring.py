a=input("enter the string ")
print("a")
b=[]
for i in a :
    print(i)
    b.append(i)
print(b)
length=len(b)
j=length-1
print(j)
str=''
while j>=0:
       str=str+b[j]
       print(b[j])
       j=j-1
print(str)
if a==str:
       print("it is a palindrome")
else:
       print("it is not a palindrome")
   
