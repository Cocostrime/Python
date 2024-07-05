Name = ["Virat","Rohit","Jaspreet","Shikhar"]
#for i in range(4):
 #   name = input("Enter name of players: ")
  #  Name.append(name)
aScore=[]
bScore=[]
cScore=[]
dScore=[]
Score=[]
print(Name)
for i in range(3):
    score1 = int(input("Enter score for Virat: "))
    aScore.append(score1)
for i in range(3):
    score2 = int(input("Enter score for Rohit: "))
    bScore.append(score2)
for i in range(3):
    score3 = int(input("Enter score for Jaspreet: "))
    cScore.append(score3)
for i in range(3):
    score4 = int(input("Enter score for Shikhar: "))
    dScore.append(score4)

Score.append(aScore)
Score.append(bScore)
Score.append(cScore)
Score.append(dScore)

print("Scores are:", Score)

sum=0
for s in Score:
    sum=0
    for i in s:
        sum +=i
    print("Sum of scores of each player : ", sum)
    
total = [0,0,0]
for s in Score:
    for i in range(3):
        total[i] += s[i]
print("Total of each match: ", total)  

manOFmatch = []
highestScore = 0
for i in range(3):
    for j in range(4):
        if Score[j][i] > highestScore:
            highestScore = Score[j][i]
            man = Name[j]
    manOFmatch.append(man)

print("Man of the Match for each match: ", manOFmatch)
