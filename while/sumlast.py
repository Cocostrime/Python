sum=0
n = int(input("Enter n: "))
sum = sum + (n%10)
n = n//10
while n>9:
    n = n//10
sum = sum+ n

print("Sum of first and last:",sum)