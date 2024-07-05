max=0
min=1
n= int(input("Enter value of n: "))
for i in range(1,n+1):
    num = int(input("Enter the number: "))
    if num>min and num<max: 
        min=num
    else:
        max=num

print("Maximum = ", max)
print("Minimum = ", min)