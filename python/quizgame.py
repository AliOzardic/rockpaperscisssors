#create a dict for questions
questions = {"question1": {
    "question": "What is the capital of Turkey" , "answer":"Ankara"
},"question2":{"question":"What is the capital of Germany" , "answer":"Berlin"
},"question3":{"question":"What is the capital of France", "answer":"Paris"
},"question4":{"question":"What is the capital of India", "answer":"New delhi"
},"question5":{"question":"Who is the leader of Russia in 2023", "answer":"putin"
},"question6":{"question":"Which continent is China in", "answer":"asia"
},"question7":{"question":"Who is the founder of Microsoft", "answer":"bill gates"
},"question8":{"question":"What is the capital of USA", "answer":"Washington"
},"question9":{"question":"What is the currency of Europe", "answer":"Euro"
},"question10":{"question":"What is the currency of USA", "answer":"dollar"
}}
#add a counter to keep the score
score = 0
#loop through the items of the dict
while True:
    for key,value in questions.items():
        #ask the question and ask for an answer from the user
        print(value["question"])
        answer = input("Answer: ")
        #compare the uer input with the real answer
        if answer.lower() ==value['answer'].lower():
            print("You are correct")
            score+=1
            print(f"Your score is :{score} ")
        else:
            print("You are wrong")
            print("Correct answer is: " + value['answer'])
            print()
            print("your score is " + str(score))
    #give user  statistics for the quiz
    print("Your final score is: " + str(score))
    print("You got: "+str(int(score/len(questions)*100)) +"% "" right ")
    #ask the user to play again 
    if not input("do you want to take the wuiz again(y or n)") == "y":
        quit()