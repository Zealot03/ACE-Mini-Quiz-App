import random
questions = [
    {
        "question": "Which data structure follows FIFO?",
        "options": ["A. Stack", "B. Queue", "C. Tree", "D. Graph"],
        "answer": "B"
    },
    {
        "question": "Which language is used to create the structure of a web page?",
        "options": ["A. Python", "B. C++", "C. HTML", "D. Java"],
        "answer": "C"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. #", "C. /*", "D. --"],
        "answer": "B"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["A. String", "B. Integer", "C. Boolean", "D. Float"],
        "answer": "C"
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "A. Central Processing Unit",
            "B. Computer Personal Unit",
            "C. Central Program Utility",
            "D. Computer Processing User"
        ],
        "answer": "A"
    },
    {
        "question": "Which data structure uses LIFO?",
        "options": ["A. Queue", "B. Stack", "C. Array", "D. Tree"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["A. function", "B. define", "C. def", "D. fun"],
        "answer": "C"
    },
    {
        "question": "Which of these is a programming language?",
        "options": ["A. Python", "B. HTML", "C. CSS", "D. HTTP"],
        "answer": "A"
    },
    {
        "question": "What does RAM stand for?",
        "options": [
            "A. Read Access Memory",
            "B. Random Access Memory",
            "C. Run Access Memory",
            "D. Random Application Memory"
        ],
        "answer": "B"
    },
    {
        "question": "Which operator is used for multiplication in Python?",
        "options": ["A. x", "B. #", "C. *", "D. %"],
        "answer": "C"
    }
]

def show_question(question, number):
    print("\nQuestion", number, "/", len(questions))
    print(question["question"])

    for option in question["options"]:
        print(option)

def start_quiz():
    score = 0

    random.shuffle(questions)

    for i in range(len(questions)):
        show_question(questions[i], i + 1)

        answer = input("Your answer: ")

        if answer.upper() == questions[i]["answer"]:
            score = score + 1
            print("Correct!")
        else:
            print("Wrong!")
            print("Correct answer:", questions[i]["answer"])

        print("Score:", score, "/", i + 1)

    return score

def show_result(score):
    print("\n===== QUIZ COMPLETE =====")

    print("Final Score:", score, "/", len(questions))

    percentage = (score / len(questions)) * 100
    print("Percentage:", percentage, "%")

    if score >= 8:
        print("Performance: Excellent!")
    elif score >= 5:
        print("Performance: Good!")
    else:
        print("Performance: Keep practicing!")
def main():
    print("===== MINI QUIZ APP =====")
    print("Answer each question using A, B, C or D.")

    score = start_quiz()
    show_result(score)
main()