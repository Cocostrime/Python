a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a>b and a>c:
    print(a ,"is the largest number",)
elif b>c and b>a:
     print(b ,"is the largest number",)
elif c>a and c>b:
     print(c ,"is the largest number",)
else:
    print("All/any two are equal")