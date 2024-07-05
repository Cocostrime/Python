names = []
for i in range(5):
    name = input("Enter the name: ")
    names.append(name)

print("Collected names:", names)

c = int(input("Enter character constraint: "))

for name in names:
    if len(name) == c:
        print(name)

