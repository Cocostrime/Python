n = int(input("Enter value of n: "))
fact = 1
sums=0
for i in range (1,n+1):
    fact = fact*i
    sums= fact+sums
print(sums)