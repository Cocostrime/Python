sum=0
n = int(input("Enter n: "))
temp=n
while n>0:
    sum = (sum*10) + (n%10)
    n = n//10

if sum==temp:
    print ("Palindrome")
else:
    print("not Palindrome")


print("Reverse = ", sum)
if sum==n:
    print ("pallindrome")