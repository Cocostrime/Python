sum=0
n = int(input("Enter n: "))
while n>0:
    sum = sum + (n%10)
    n = n//10
print("Sum of digits = ", sum)