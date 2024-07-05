d = int(input("Enter days: "))
years = d//365
DL = d%365
print("converted to years: " , years)
months = DL//30
print("converted to months: ", months)
dayLeft = DL%30
print("converted to left days: ", dayLeft)