para = input("Enter your paragraph: ")
words=[]
list1 = para.split()
print(list)

for word in list1:
    if word not in words:
        words.append(word)
        print(word,list1.count(word))

for word in list1:
        if word==word [::-1]:
            print(word,"Is pallindrome")
        else:
            print(word,"Not a pallindrome ")