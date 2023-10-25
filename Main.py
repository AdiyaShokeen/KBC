questions = {
    "question1":["opt1","opt2","opt3","opt4"],
    "question2":["opt1","opt2","opt3","opt4"],
    "question3":["opt1","opt2","opt3","opt4"],
    "question4":["opt1","opt2","opt3","opt4"],
    "question5":["opt1","opt2","opt3","opt4"],
    "question6":["opt1","opt2","opt3","opt4"],
    "question7":["opt1","opt2","opt3","opt4"],
    "question8":["opt1","opt2","opt3","opt4"],
}

answers = ["b","b","b","b","b","a","a","d"]

# for i,q in enumerate(questions.items()):
#     print(q[0],":")
#     print(q[1][0],",",q[1][1])
#     print(q[1][2],",",q[1][3])

i = 0
while i<len(questions):
    l = [(q,o) for q,o in questions.items()]
    print(l[i][0])
    print(f"a.{l[i][1][0]}, b.{l[i][1][1]}")
    print(f"c.{l[i][1][2]}, d.{l[i][1][3]}")
    ans = input("endter your answer : ")
    if answers[i] == ans:
        print("You Are Correct")
    else:
        print("You are Wrong")
        break
    i += 1