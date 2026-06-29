"""questions={
    "What is the name of your city?": "okara",
    "2+2=?": "4",
    "python kya hai?": "programming language"
}
score=0
for question,answer in questions.items():
    player=input(question).lower()
    if player==answer:
        score+=1
        print("correct")
    else:
        print(f"wrong! correct answer is {answer}")

    print(f"Tumhara score: {score}/{len(questions)}") """
questions={
    "What is the name of your city?": "okara",
    "python kya hai?":"programming language",
    "2+2=?": "4"
}
score=0
for question,answer in questions.items():
    player=input(question)
    if player==answer:
        score+=1
        print("correct")
    else:
        print(f"wrong! correct answer is {answer}")

    print(f"your score is {score}/{len(questions)}")