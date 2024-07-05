marks = []
aMarks = []
bMarks = []

for i in range(3):
    mark1 = int(input("Enter marks for student a: "))
    aMarks.append(mark1)
for i in range(3):
    mark2 = int(input("Enter marks for student b: "))
    bMarks.append(mark2)

marks.append(aMarks)
marks.append(bMarks)
print("Marks are:", marks)

sum=0
for m in marks:
    sum=0
    for i in m:
        sum +=i
    print("Sum of marks of each student : ", sum)

total = [0,0,0]
for m in marks:
    for i in range(3):
        total[i] += m[i]
print("Total of each subject: ", total)  