n = int(input("Enter the number of subjects: "))
m = int(input("Enter the number of students: "))
grades = []

for student in range(m):
    student_grades = []
    print(f"Enter grades for student {student + 1}:")
for subject in range(n):
    grade = int(input(f"  Subject {subject + 1}: "))
    student_grades.append(grade)
grades.append(student_grades)

# Calculate total marks for each student
student_totals = [sum(student_grades) for student_grades in grades]

# Calculate total marks for each subject
subject_totals = [sum(grades[student][subject] for student in range(m)) for subject in range(n)]

# Print the initial grades list
print("\nGrades List:")
for student_grades in grades:
    print(student_grades)

# Print total marks for each student
print("\nTotal Marks for Each Student:")
for i, total in enumerate(student_totals):
    print(f"Student {i + 1}: {total}")

# Print total marks for each subject
print("\nTotal Marks for Each Subject:")
for i, total in enumerate(subject_totals):
    print(f"Subject {i + 1}: {total}")
