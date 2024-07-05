prizemoney = 0
quesbank = [[1 , "Who was the lead actress in Lagaan?", "Gracy Singh", "Katrina Kaif","Kareena Kapoor","Kajol","Gracy Singh"],
            [2 , "Who was the lead actor in Haider?", "Shahid Kapoor", "Hritik Roshan","Ranbir Kapoor","Ajay Devgan","Shahid Kapoor"],
            [3 , "Who is Sonakshi Sinha's husband?", "Iqbal Khan", "Salman Khan","Ajay Devgan","Karan Kundra","Iqbal Khan"],
            [4 , "Who is Ranveer Singh's wife?", "Vani Kapoor", "Alia Bhatt","Anushka Sharma","Deepika Padukone","Deepika Padukone"],
            [5 , "Who is the lead actress in Kalki?", "Khushi Kapoor","Annanya Pandey","Deepika Padukone", "Kajol","Deepika Padukone"],
            [6 , "Who is Saif Ali Khan's Wife?", "Amrita Singh", "Preeti Zinta","Kareena Kapoor","Tamanah Bhatia","Kareena Kapoor"],
            [7 , "Who played Akshay Kumar's mother's role in Waqt", "Priyanka Chopra", "Madhuri Dixit","Shefali Shah","Twinkle Khanna","Shefali Shah"],
            [8 , "Who played the role of Vedha in Vikram Vedha?", "Saif Ali Khan", "Hritik Roshan","Kapil Sharma","Karan Kundra","Hritik Roshan"],
            [9 , "Who played the role of Radhika in Prem Ratan Dhan Payo?", "Sonam Kapoor", "Swara Bhaskar","Aashita Bhatia","Samaira Rao","Aashita Bhatia"],
            [10 , "Who was the lead actor in Kambaqt Ishq?", "Aamir Khan","Arjun Rampal","Akshay Kumar", "Arbaaz Khan","Akshay Kumar"]]

for que in quesbank:
    print("Question: ", que[0],":", que[1])
    for i in range(2,6):
        print(que[i])
    print("What is your answer?")
    ans = input()
    if ans == que[-1]:
        print("YAY! CORRECT ANSWER")
        prizemoney += 100
    else:
        print("OOP! WRONG ANSWER")
        prizemoney -= 50
print("You won: ", prizemoney)
