a = int(input("Enter the number: "))
if a%5==0 and a%7==0:
    print("The number is divisible by both 5 and 7.")
elif a%5==0:
    print("The number is divisible by only 5.")
elif a%7==0:
    print("The number is divisible by only 7.")
else:
    print("The number is not divisible by 5 or 7.")