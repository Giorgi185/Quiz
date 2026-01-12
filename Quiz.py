questions = {
    "Easy": [
        {"question": "რომელ ქვეყანას ეკუთვნის ეიფელის კოშკი?", "answer": "საფრანგეთი"},
        {"question": "რომელია ყველაზე პატარა ქვეყანა?", "answer": "ვატიკანი"},
        {'question': 'რომელია ყველაზე ცნობილი ნახატი? ', 'answer': 'მონა ლიზა'},
        {'question': 'ვისი ნაწარმოებია რომეო და ჯულიეტა?(მხოლოდ გვარი)', 'answer': 'შექსპირი'},
        {'question': 'რომელია ყველაზე გავრცელებული რელიგია?', 'answer': 'ქრისტიანობა'}
    ],
    "Medium": [
        {"question": "რომელია მზის სისტემაში ბოლო პლანეტა? ", "answer": "ნეპტუნი"},
        {"question": "რომელ რელიგიაში ვხვდებით ღმერთ შივას? ", "answer": "ინდუიზმი"},
        {'question': 'ვინ შექმნა ქიმიურ ელემენტთა ცხრილი?(მხოლოდ გვარი) ', 'answer': 'მენდელეევი'},
        {'question': 'დეკემბრის რომელ რიცხვში აღნიშნავს კათოლიკური ეკლესია შობას?(ციფრებით შეიყვანეთ პასუხი) ',
         'answer': '25'},
        {'question': 'რომელ წელს დაიწყო მეორე მსოფლიო ომი?(ციფრებით შეიყვანეთ პასუხი) ', 'answer': '1939'},
        {'question': 'რომელია ყველაზე მძიმე ცხოველი?(ორი სიტყვა)', 'answer': 'ლურჯი ვეშაპი'},
        {'question': 'თებერვლის რომელი დღე დგება მხოლოდ ოთხ წელიწადში ერთხელ?(ციფრებით შეიყვანეთ პასუხი) ',
         'answer': '29'},
        {'question': 'დაასახელეთ აშშ-ს დედაქალაქი', 'answer': 'ვაშინგტონი'},
        {'question': 'რომელ წელს დასრულდა ცივი ომი?(ციფრებით შეიყვანეთ პასუხი)', 'answer': '1991'},
        {'question': 'დაასახელეთ ყველაზე დიდი ქვეყანა ჩრდილოეთ ამერიკაში', 'answer': 'კანადა'}
    ],
    "Hard": [
        {"question": "რა ქვია ციყვის ნაშიერს? ", "answer": "დღნაშვი"},
        {"question": "რომელ წელს აღმოაჩინეს ამერიკა?(ციფრებით შეიყვანეთ პასუხი) ", "answer": "1492"},
        {'question': 'დაასახელეთ ქვეყანა, რომელსაც ყველაზე მეტი ვულკანი აქვს ევროპაში', 'answer': 'ისლანდია'},
        {'question': 'რომელი თეორიის ავტორია ალბერტ აინშტაინი? ', 'answer': 'ფარდობითობის'},
        {'question': 'რომელ საუკუნეში გავრცელდა შავი ჭირი?(ციფრებით შეიყვანეთ პასუხი) ', 'answer': '14'},
        {'question': 'რომელია ყველაზე საშიში ფილმი? ', 'answer': 'ეგზორცისტი'},
        {'question': 'დაასახელეთ ყველაზე ბედნიერი ქვეყანა ', 'answer': 'ფინეთი'},
        {'question': 'რომელ ქვეყანაში გამოიგონეს ჭადრაკი? ', 'answer': 'ინდოეთი'},
        {'question': 'დაასახელეთ რობერტ როდრიგესის ფილმი, რომელიც 18 ნოემბერს, 2115წელს გამოვა(ორი სიტყვა) ',
         'answer': '100 წელი'},
        {'question': 'რომელ წელს დაიწერა აშშ-ს დამოუკიდებლობის დეკლარაცია?(ციფრებით შეიყვანეთ '
                     'პასუხი) ', 'answer': '1776'},
        {'question': 'ვინ იყო აშშ-ს მე-16 პრეზიდენტი?(სახელი,გვარი)', 'answer': 'აბრაამ ლინკოლნი'},
        {'question': 'დაასახელეთ ცოცხალი ორგანიზმის კლონირების პირველი შემთხვევა(ორი სიტყვა)',
         'answer': 'ცხვარი დოლი'},
        {'question': 'როგორ იშიფრება დნმ?(ორი სიტყვა) ', 'answer': 'დეზოქსირიბონუკლეინის მჟავა'},
        {"question": "ვისი სიტყვებია 'მე ვიცი, რომ არაფერი ვიცი.' ?", 'answer': 'სოკრატე'},
        {'question': 'რა არის ყველაზე სწრაფი?', 'answer': 'სინათლე'}

    ]
}

level_requirements = {
    'Easy': 3,
    'Medium': 6,
    'Hard': 10
}

unlocked_levels = {
    "Easy": True,
    "Medium": False,
    "Hard": False
}

def play_quiz(level_questions):
    score = 0

    for q in level_questions:
        attempts = 3

        while attempts > 0:
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
                break
            else:
                attempts -= 1
                if attempts > 0:
                    print(f"არასწორია! დარჩენილი ცდები: {attempts}")
                else:
                    print(f"ცდები ამოიწურა! სწორი პასუხი იყო: {q['answer']}")

    print(f"Quiz დასრულდა! ქულა: {score} / {len(level_questions)}")
    return score


while True:
    print("აირჩიე დონე:")
    print("1. Easy")
    if unlocked_levels["Medium"]:
        print("2. Medium")
    else:
        print("2. Medium locked")

    if unlocked_levels["Hard"]:
        print("3. Hard")
    else:
        print("3. Hard locked")

    print("4. გამოსვლა")

    choice = input("შეიყვანე არჩევანი: ")

    if choice == "1":
        score = play_quiz(questions["Easy"])
        if score >= level_requirements["Easy"]:
            print("Easy დონე დახურე გილოცავ")
            unlocked_levels["Medium"] = True
        else:
            print("Easy დონე ვერ დახურე")
    elif choice == "2":
        if not unlocked_levels["Medium"]:
            print("ეს დონე ჯერ არ გაქვს გახსნილი")
            continue
        score = play_quiz(questions["Medium"])
        if score >= level_requirements["Medium"]:
            print("Medium დონე დახურე გილოცავ")
            unlocked_levels['Hard'] = True
        else:
            print("Medium დონე ვერ დახურე")
    elif choice == "3":
        if not unlocked_levels["Hard"]:
            print("ეს დონე ჯერ არ გაქვს გახსნილი")
            continue
        score = play_quiz(questions["Hard"])
        if score >= level_requirements["Hard"]:
            print("Hard დონე დახურე გილოცავ")
            print("გილოცავ თამაში მთლიანად დახურე")
        else:
            print("Hard დონე ვერ დახურე")
    elif choice == "4":
        print("ნახვამდის")
        break
    else:
        print("არასწორი არჩევანი, სცადე თავიდან")