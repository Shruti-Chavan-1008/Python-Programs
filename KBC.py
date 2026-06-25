# KBC Python Quiz Game A simple console-based quiz game created using Python.

## How Program Works

"""- The game starts by displaying Question 1.
- Each question has four options (A, B, C, D).
- The user enters the correct option.
- If the answer is correct:
  - The user moves to the next question.
  - Prize money increases.
- If the answer is wrong:
  - The game stops.
- The game continues until Question 10.
- After completing all questions, the final winning amount is displayed."""

 

## Run Project

#```bash
#python kbc.py


questions = [
    "What is the capital of India?",
    "Which planet is known as the Red Planet?",
    "Who is known as the Father of Computers?",
    "Which is the largest ocean in the world?",
    "How many players are there in one cricket team?",
    "Which gas do plants absorb during photosynthesis?",
    "Who wrote the Indian National Anthem?",
    "Which programming language is mostly used for AI and Data Science?",
    "Which is the fastest land animal?",
    "Who is the founder of Microsoft?"
]


options = [
    ["A) Mumbai", "B) New Delhi", "C) Kolkata", "D) Chennai"],

    ["A) Earth", "B) Jupiter", "C) Mars", "D) Venus"],

    ["A) Charles Babbage", "B) Alan Turing", "C) Bill Gates", "D) Steve Jobs"],

    ["A) Atlantic Ocean", "B) Indian Ocean", "C) Pacific Ocean", "D) Arctic Ocean"],

    ["A) 9", "B) 10", "C) 11", "D) 12"],

    ["A) Oxygen", "B) Carbon Dioxide", "C) Nitrogen", "D) Hydrogen"],

    ["A) Mahatma Gandhi", "B) Rabindranath Tagore",
     "C) Jawaharlal Nehru", "D) Subhash Chandra Bose"],

    ["A) HTML", "B) Python", "C) CSS", "D) XML"],

    ["A) Lion", "B) Tiger", "C) Cheetah", "D) Horse"],

    ["A) Elon Musk", "B) Bill Gates",
     "C) Mark Zuckerberg", "D) Jeff Bezos"]
]


answers = [
    "B",
    "C",
    "A",
    "C",
    "C",
    "B",
    "B",
    "B",
    "C",
    "B"
]


money = 0


print("🔥 Welcome to KBC Quiz Game 🔥")


for i in range(len(questions)):

    print("--------------------------------")
    print("Q", i+1, questions[i])

    for option in options[i]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ")

    if user_answer.upper() == answers[i]:

        money = money + 500

        print("Correct Answer 🎉")
        print("You won ₹", money)

    else:

        print("Wrong Answer ❌")
        print("Game Over")
        break


print("--------------------------------")
print("Your total winning amount is ₹", money)