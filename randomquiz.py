QUESTIONS = {
    "When was Windows 10 released?": [
        "2016", "2015", "2018", "2017", "2019"
    ],
    "What platforms do I not use?": [
        "Twitter", "Pinterest", "Discord", "YouTube", "Steam"
    ],
    "What was my first repository?": [
        "random-quiz-game", "example-webpage",
    ],
    "What is my webpage made out of?": [
        "HTML only", "HTML and CSS",
    ],
    "What is my GitHub name?": [
        "Sussy Bob",
        "bob1774",
        "SussyBob420",
    ],
}

for question, alternatives in QUESTIONS.items():
    correct_answer = alternatives[1]
    for alternative in sorted(alternatives):
        print(f"  - {alternative}")

    answer = input(f"{question}? ")
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")