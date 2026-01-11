questions = {
    "Easy": [
        {"question": "რა ფერია მზე?", "answer": "ყვითელი"},
        {"question": "რა ფერია ცა?", "answer": "ჩისფერი"}
    ],
    "Medium": [
        {"question": "5 * 5 ...?", "answer": "25"},
        {"question": "8 + 9 ...?", "answer": "17"}
    ],
    "Hard": [
        {"question": "რამდენია 15 * 12?", "answer": "180"},
        {"question": "რა არის წყლის ფორმულა?", "answer": "H2O"}
    ]
}

def play_quiz(level_questions):
    score = 0
    for q in level_questions:
        print(q["question"])
        answer = input("პასუხი: ")
        correct_letters = []
        for i, (user_char, correct_char) in enumerate(zip(answer, q["answer"])):
            if user_char == correct_char:
                correct_letters.append((i, user_char))
        if correct_letters:
            print("სწორ ადგილზეა:")
            for i, char in correct_letters:
                print(f"  პოზიცია {i}: '{char}'")
        else:
            print("არცერთი ასო არ არის სწორ ადგილზე")
        if answer == q["answer"]:
            print("სწორი პასუხი!")
            score += 1
        else:
            print(f" არასწორი პასუხი! სწორი პასუხი: {q['answer']}")
    print(f"\n Quiz დასრულდა! ქულა: {score} / {len(level_questions)}")

while True:
    print("\nაირჩიე დონე:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. გამოსვლა")
    choice = input("შეიყვანე არჩევანი: ")
    if choice == "1":
        play_quiz(questions["Easy"])
    elif choice == "2":
        play_quiz(questions["Medium"])
    elif choice == "3":
        play_quiz(questions["Hard"])
    elif choice == "4":
        print("ნახვამდის!")
        break
    else:
        print("არასწორი არჩევანი, სცადე ისევ!")
