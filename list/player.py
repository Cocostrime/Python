players = []
skills = []
result1 = ["Batter: "]
result2 = ["Ballers: "]

print("Names:-")
for i in range(5):
    player = input("Enter name: ")
    players.append(player)
print("Skills:-")
for i in range(5):
    skill = input("Enter skills: ")
    skills.append(skill)    
print(players)
print(skills) 

print("Result:-")             
for i in range(5):
    if skills[i]=="Bat":
        result1.append(players[i])
    else:
        result2.append(players[i])
print(result1)
print(result2)