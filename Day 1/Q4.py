# Write a program to Count digits in a number
N=int (input("Enter a number:"))
count=0
temp=N
while N !=0:
    if temp/10!=0:
        count=count+1
    else:
        print(count)