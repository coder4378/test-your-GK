print("Hello, welcome to the GK quiz!")
ready=input("are you ready to play(yes/no): ")
score=0
total_q = 4
if ready.lower() == "yes":
    ans1 = input("is silver fish an insect (True/False)?")
if ans1.lower() == "False":
    score+=1
    print("correct")
else : print("incorrect it is an insect")
ans2 = input("which is largest land animal?")
if ans2.lower() == "elephant":
        print("correct")
        score+=1
else : print("it is elephant")

ans3 = input("in which year does covid 19 came in china?")
if ans3.lower() == "2019":
        print("correct")
        score+=1
else : print("incorrect it came un 2019")

ans4 = input("when did India win 1st world cup?")
if ans1.lower() == "1983":
        print("correct")
        score+=1
else : print("incorrect 1983")
print("Thank you for playing you got", score , "question correct")
mark=(score/total_q)*100
print("Marks", mark, "%")

print("Good By")
      
