# Write a program to Calculate sum of first N natural numbers.
N=int (input("Enter the number:"))
sum=0
for i in range(1,N+1):
  sum=sum+i
print("The desired sum is :",N)
