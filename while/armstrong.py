sum=0
n = int(input("Enter n: "))
temp=n
while n>0:
    sum = sum + (n%10)**3
    n = n//10

print("sum of cubes of each digit = ", sum)
if temp==sum:
    print("Armstrong")
else:
    print("not armstrong")