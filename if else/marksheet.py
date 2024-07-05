print("Maximum marks possible = 500")
s1 = int(input("Enter marks for first subject: "))
s2 = int(input("Enter marks for second subject: "))
s3 = int(input("Enter marks for third subject: "))
s4 = int(input("Enter marks for forth subject: "))
s5 = int(input("Enter marks for fifth subject: "))

total= s1+s2+s3+s4+s5
percentage= (total/500)*100

if s1>33 and s2>33 and s3>33 and s4>33 and s5>33:   
    print("PASS") 
    print("Total marks obtained= ", total)
    print("Percentage = ", percentage)
    if 85<percentage<=100: 
        print("Grade obtained is A")
    elif 70<percentage<=85:
        print("Grade obtained is B")
    elif 55<percentage<=70:
        print("Grade obtained is C")
    elif 40<percentage<=55:
        print("Grade obtained is D")
    elif 33<=percentage<=40:
        print("Grade obtained is P")
    else:
        print("Grade obtained is F")
else: 
    print("FAIL")
    print("Not eligible for any grades and percentage.")