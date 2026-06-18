# Write a program to Find factorial of a number
N=int (input("Enter a number:"))
fact=1
i=1
while (i<=N):
    fact=fact*i
    i=i+1
print(fact)