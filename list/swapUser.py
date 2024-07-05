l1 = []
for i in range(5):
    list=int(input("Enter elements: "))
    l1.append(list)
print(l1)
v1 = int(input("Enter first value to be swapped: "))
v2 = int(input("Enter second value to be swapped: "))

for i in range (5):
    if l1[i]==v1:
        I1=i
    if l1[i]==v2:
        I2=i    
    
print("Swapped: ")
l1[I1],l1[I2] = l1[I2],l1[I1]
print(l1)