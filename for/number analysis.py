sum=0
even=0
odd=0
max=0
min=0
n= int(input("Enter value of n: "))
for i in range(1,n+1):
    num = int(input("Enter the number: "))
    if i==1:
        min=num
        max=num
    sum = sum+num
    
    if num%2==0:
        even = even+1
    else:
        odd = odd+1
    if num<min:
         min=num
    if num>max: 
        max=num

print("SUM = ", sum)
print("Odd = ", odd)
print("Even = ", even)
print("Maximum = ", max)
print("Minimum = ", min)