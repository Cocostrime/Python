l1=[2,3,4,2,3,4,5,5]
for i in range(len(l1)):
    for j in range(i):
        if l1[i]==l1[j]:
            print(l1[j])