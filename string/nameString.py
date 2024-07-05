name = "palgor"
vowels="aeiou"
print(len(name))
print(name[-1::-1])

vowel=0
consonent=0

for ch in name:
    if ch in vowels:
        vowel += 1
    else:
        consonent +=1
    

print("Vowels: ", vowel)
print("Consonent: ", consonent)