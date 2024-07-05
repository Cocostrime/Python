month = int(input("Enter the month number: "))
if month>=1 and month<=3:
    print("The month is in first quarter.")
elif month>=4 and month<=6:
    print("The month is in second quarter.")
elif month>=7 and month<=9:
    print("The month is in third quarter.")
elif month>=10 and month<=12:
    print("The month is in forth quarter.")
else:
    print("Invalid month number")