import json
import os

def save_results(filename, new_results, difficulty):          # save results on .json file
    try:
        with open(filename, "r") as f:
            existing_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []

    # remove previous results of the same difficulty
    existing_data = [item for item in existing_data if item.get("difficulty") != difficulty]

    existing_data.extend(new_results)

    with open(filename, "w") as f:
        json.dump(existing_data, f, indent=4)

def load_results(filename, difficulty=None):                 # load results from previous games on .json file
    try:
        with open(filename, "r") as f:
            data = json.load(f)

            if difficulty:
                data = [item for item in data if item.get("difficulty") == difficulty]

            if not data:
                print(f"No results found for '{difficulty}' difficulty." if difficulty else
                      "No results found.")
                return
            for i, item in enumerate(data, 1):
                print(f"\nQuestion {i}: {item['question']}")
                if "choices" in item:
                    for idx, choice in enumerate(item["choices"], 1):
                        print(f" {idx}. {choice}")
                print(f"Your answer: {item['your_answer']} - {'Correct' if item['is_correct'] else 'Incorrect'}")
                print(f"Correct answer: {item['correct_answer']}")
    except FileNotFoundError:
        print('No previous results found.')


def get_answer(question_text, prompt, valid_choices=None):       # function to streamline user choice restrictions
    while True:
        print(question_text)
        answer = input(prompt).strip()
        if not answer:
            print("Input cannot be empty. Please try again.")
        elif valid_choices and answer not in valid_choices:
            print(f'Please pick between one of the given options.')
        else:
            return answer

easy_questions = [     # Putting the questions in dictionaries
    {
        "question": 'What is the capital of Germany?',
        "choices": ["1. Munich", "2. Berlin", "3. Frankfurt am Main", "4. Hamburg"],
        "answer": "2"
    },
    {
        "question": "Who was Chancellor of Germany during World War II?",
        "choices": ["1. Angela Merkel", "2. Olaf Schulz", "3. Otto von Bismarck",
                    "4. Adolf Hitler"],
        "answer": "4"
    },
    {
        "question": "Which were the two Major Powers opposing each other during the"
                    " Cold War?",
        "choices": ["1. USA/USSR", "2. Germany/Austria", "3. Italy/Spain",
                    "4. North Africa/ South Africa"],
        "answer": "1"
    },
    {
        "question": "Which individual received most of the blame for the \n"
                    "attack on the World Trade Center on Sept. 11th, 2001?",
        "choices": ["1. Muammar Gaddafi", "2. Muhammad Ali", "3. Osama bin Laden", "4. Sadam Hussein"],
        "answer": "3"
    },
    {
        "question": "Which system did the German philosopher Karl Marx write about for most \n"
                    "of his life?",
        "choices": ["1. Communism", "2. Socialism", "3. Capitalism", "4. Feudalism"],
        "answer": "3"
    },
    {
        "question": "Who invented the iPhone?",
        "choices": ["1. Bill Gates", "2. Tim Apple", "3. Workers at Apple", "4. Steve Jobs"],
            "answer": "3"
    },
    {
        "question": "Which country is the only country in the history of the world to use \n"
                    "an atom bomb?",
        "choices": ["1. Russia", "2. USA", "3. Germany", "4. United Kingdom"],
        "answer": "2"
    },
    {
        "question": "As of 2025, how many years has the U.S. been engaged in a war with \n"
                    "other countries in the world?",
        "choices": ["1. 24", "2. 7", "3. The U.S. has not been at war recently", "4. 12"],
        "answer": "1"
    }
]

normal_questions = [
    {
        "question": "What year did the Berlin Wall fall?",
        "choices": ["1. 1987", "2. 1989", "3. 1991", "4. 1993"],
        "answer": "2"
    },
    {
        "question": "Who was the first Chancellor of West Germany after World War II?",
        "choices": ["1. Otto von Bismarck", "2. Konrad Adenauer", "3. Helmut Kohl", "4. Willy Brandt"],
        "answer": "2"
    },
    {
        "question": "How many assassination attempts did the U.S. make on Fidel Castro \n"
                    "after the Cuban Revolution?",
        "choices": ["1. Around 10", "2. Around 50", "3. Around 100", "4. Over 600"],
        "answer": "4"
    },
    {
        "question": "What is one major reason the U.S government has supported coups \n"
                    "in Latin America during the 20th century?",
        "choices": ["1. To protect U.S. corporate interests", "2. To support anti-communist regimes",
                    "3. To promote democracy", "4. To prevent terrorism"],
        "answer": "1"
    },
    {
        "question": "Which term is often used to describe the close relationship \n"
                    "between weapons manufacturers and political power in the U.S.?",
        "choices": ["1. Capitalist Core", "2. Economic Hegemony",
                    "3. Military-Industrial Complex", "4. Security Alliance"],
        "answer": "3"
    },
    {
        "question": "Which of the following countries has been under heavy sanctions \n"
                    "by the U.S. despite not posing a direct military threat?",
        "choices": ["1. North Korea", "2. Iran", "3. Venezuela", "4. Russia"],
        "answer": "3"
    },
    {
        "question": "Why did whistleblower Edward Snowden flee the United States in 2013?",
        "choices": ["1. He was evading taxes", "2. He mocked Trump for his small hands",
                    "3. He leaked documents exposing global surveillance by the NSA",
                    "4. He stole military secrets"],
        "answer": "3"
    },
    {
        "question": "Which event is often cited as a false pretext for \nthe U.S. "
                    "invasion of Iraq in 2003?",
        "choices": ["1. Iran's nuclear program", "2. Weapons of Mass Destruction(WMDs)",
                    "3. Saddam Hussein's invasion of Kuwait", "4. The 9/11 attacks"],
        "answer": "2"
    },
    {
        "question": "Which country has the highest number of military \n"
                    "bases outside its own territory?",
        "choices": ["1. China", "2. Russia", "3. France", "4. United States"],
        "answer": "4"
    },
    {
        "question": "Which country has faced widespread international criticism \n"
                    "for its military actions and blockade policies in a \n"
                    "territory, where nearly half the population are children \n"
                    "and living conditions have been described by many as resembling\n"
                    " an open-air prison?",
        "choices": ["1. Israel", "2. Syria", "3. Egypt", "4. Iran"],
        "answer": "1"
    }
]

hard_questions = [
    {
        "question": "Which economic system places profit and private ownership at \n"
                    "the center, often resulting in exploitation of the working class?",
        "choices": ["1. Socialism", "2. Capitalism", "3. Feudalism", "4. Anarchism"],
        "answer": "2"
    },
    {
        "question": "Which global financial institution has been widely \n"
                    "criticized for imposing austerity measures on developing \n"
                    "countries, leading to deep economic hardship for their populations?",
        "choices": ["1. The World Bank", "2. The International Monetary Fund(IMF)",
                    "3. United Nations", "4. World Trade Organization(WTO)"],
        "answer": "2"
    },
    {
        "question": "Which major historical event was largely influenced by \n"
                    "Western powers drawing arbitrary borders, contributing to long-term \n"
                    "conflict and instability in the affected region?",
        "choices": ["1. The Fall of the Berlin Wall", "2. The Marshall Plan",
                    "3. The Formation of the European Union", "4. The Partition of India"],
        "answer": "4"
    },
    {
        "question": "Which modern country is known for providing universal healthcare and \n"
                    "has a higher quality of life for its citizens compared to more developed nations?",
        "choices": ["1. United States", "2. Brazil", "3. Cuba", "4. Australia"],
        "answer": "3"
    },
    {
        "question": "Which concept critiques the rise of corporate power in democratic governments, \n"
                    "arguing that corporate elites hold undue influence over policies that should be \n"
                    "in the interest of the people?",
        "choices": ["1. Plutocracy", "2. Democracy", "3. Oligarchy", "4. Socialism"],
        "answer": "1"
    },
    {
        "question": "According to a 2021 report by Oxfam, how much wealth did the world's 10 richest \n"
                    "men gain during the COVID-19 pandemic?",
        "choices": ["1. $10 billion", "2. $50 billion", "3. $250 billion", "4. $500 billion"],
        "answer": "4"
    },
    {
        "question": "Which one of these global corporations has been accused of exploiting workers \n"
                    "in the Global South by paying low wages and violating labor rights?",
        "choices": ["1. Starbucks", "2. Amazon", "3. Nike", "4. Apple"],
        "answer": "3"
    },
    {
        "question": "Which policy, implemented by the United States and its allies, is often seen \n"
                    "as a form of modern-day imperialism, where military force is used to secure \n"
                    "resources and maintain control over developing nations?",
        "choices": ["1. The Marshall Plan", "2. The Monroe Doctrine", "3. The War on Terror", "4. Colonialism"],
        "answer": "3"
    },
    {
        "question": "Which modern political and economic ideology is primarily concerned with \n"
                    "reducing wealth inequality, promoting social justice, and providing public \n"
                    "goods like healthcare and education?",
        "choices": ["1. Social democracy", "2. Fascism", "3. Neoliberalism", "4. Libertarianism"],
        "answer": "1"
    },
    {
        "question": "Which labor movement of the 19th century played a crucial role in establishing \n"
                    "workers' rights and labor laws in capitalist countries, including the eight-hour workday?",
        "choices": ["1. The Chartist Movement", "2. The Industrial Workers of the World(IWW)", "3. The Labor Unions",
                    "4. The Suffragette Movement"],
        "answer": "2"
    },
    {
        "question": "Which of the following is a major contributor to global carbon emissions, \n"
                    "despite outsourcing much of its production to poorer nations?",
        "choices": ["1. Brazil", "2. India", "3. United States", "4. China"],
        "answer": "3"
    },
    {
        "question": "Which historical movement sought to challenge colonial powers and empower the oppressed peoples in colonized nations by calling for self-determination and independence?",
        "choices": ["1. The Nationalist Movement of the 19th Century", "2. The Non-Aligned Movement",
                    "3. The Civil Rights Movement", "4. The Pan-African Movement"],
        "answer": "4"
    }
]

bonus_hard_question = [
    {
        "question": "Which government organization sent anonymous letters to\n"
                          "Martin Luther King Jr. urging him to commit suicide,\n"
                          "shortly before his assassination?",
        "choices": ["1. Central Intelligence Agency(CIA)", "2. Federal Bureau of Investigation(FBI)",
                    "3. National Security Agency(NSA)", "4. Department of Justice(DOJ)"],
        "answer": "2"
    }
]

def play_easy():                    # functions to start easy/normal/hard quizz
    correct_easy = 0                # score tally
    incorrect_easy = 0
    results = []

    for q in easy_questions:
        formatted = f"{q['question']}\n" + "\n".join(q['choices'])
        user_answer = get_answer(formatted, "Answer (1-4): ", ["1", "2",
                                                               "3", "4", "quit"]).lower()
        if user_answer == "quit":
            print("Quiz exited. No results saved.")
            return
        is_correct = user_answer == q['answer']
        if is_correct:
            correct_easy += 1
        else:
            incorrect_easy += 1
        results.append({
            "difficulty": "easy",
            "question": q["question"],
            "choices": q["choices"],
            "your_answer": user_answer,
            "correct_answer": q["answer"],
            "is_correct": is_correct
        })
    print(f"You got {correct_easy} correct and {incorrect_easy} incorrect.")
    quizz_completed = True
    if correct_easy == 8:
        print('Excellent! You got them all right!')
    elif correct_easy >= 5:
        print('Very good!')
    elif correct_easy >= 1:
        print('Maybe you should try again.')
    else:
        print('You should learn more about the world.')

    if quizz_completed:
        save_results(results_file, results, difficulty="easy")

def play_normal():
    correct_normal = 0
    incorrect_normal = 0
    results = []
    for q in normal_questions:
        formatted = f"{q['question']}\n" + "\n".join(q['choices'])
        user_answer = get_answer(formatted, "Answer (1-4): ", ["1", "2",
                                                               "3", "4"])
        is_correct = user_answer == q['answer']
        if is_correct:
            correct_normal += 1
        else:
            incorrect_normal += 1
        results.append({
            "difficulty": "normal",
            "question": q["question"],
            "choives": q["choices"],
            "your_answer": user_answer,
            "correct_answer": q["answer"],
            "is_correct": is_correct
        })
    print(f"You got {correct_normal} correct and {incorrect_normal} incorrect.")
    if correct_normal == 10:
        print('Excellent! You got them all right!')
    elif correct_normal >= 7:
        print('Very good!')
    elif correct_normal >= 4:
        print('Good.')
    elif correct_normal >= 1:
        print('Maybe you should try again.')
    else:
        print('You should learn more about the world.')
    save_results(results_file, results)

def play_hard():
    correct_hard = 0
    incorrect_hard = 0
    results = []

    for q in hard_questions:
        formatted = f"{q['question']}\n" + "\n".join(q['choices'])
        user_answer = get_answer(formatted, "Answer (1-4):", ["1", "2",
                                                              "3", "4"])
        is_correct = user_answer == q['answer']
        if is_correct:
            correct_hard += 1
        else:
            incorrect_hard += 1
        results.append({
            "difficulty": "hard",
            "question": q["question"],
            "choices": q["choices"],
            "your_answer": user_answer,
            "correct_answer": q["answer"],
            "is_correct": is_correct
        })
    if correct_hard >= 7:
        print("You got enough points to get a Bonus Question.")
        chance = ('Would you like to try the Bonus Question?')
        chance_answer = get_answer(chance, "Yes or No (y/n): ", ["y", "n"])
        if chance_answer == "y":
            for q in bonus_hard_question:
                bonus_formatted = f"{q['question']}\n" + "\n".join(q['choices'])
                bonus_user_answer = get_answer(bonus_formatted, "Answer (1-4): ",
                                               ["1", "2", "3", "4"])
                is_correct_b = bonus_user_answer == q['answer']
                if is_correct_b:
                    correct_hard += 1
                else:
                    incorrect_hard += 1
                results.append({
                    "difficulty": "hard",
                    "question": q["question"],
                    "your_answer": bonus_user_answer,
                    "correct_answer": q["answer"],
                    "is_correct": is_correct_b,
                    "is_bonus": True
                })
    elif correct_hard < 7:
        print("You didn't get enough points to try the Bonus Question.")
    print(f"You got {correct_hard} correct and {incorrect_hard} incorrect.")

    if correct_hard > 12:
        print('You did exceptionally well!')
    elif correct_hard == 12:
        print('Excellent! You got them all right!')
    elif correct_hard >= 9:
        print('Very good!')
    elif correct_hard >= 6:
        print('Good.')
    elif correct_hard >= 1:
        print('Maybe you should try again.')
    else:
        print('You should learn more about the world.')

    save_results(results_file, results)




username = get_answer("Log-in/Create an account.", "Username: ").strip().lower()
results_file = f"{username}_results.json"

if os.path.exists(results_file):
    print(f"Welcome back to the quizz, {username}!")
else:
    print(f"Hello, {username}! Welcome to your first quizz.")
while True:
    print("Please choose a difficulty level.\nEasy - 8 easy questions.\nNormal - 10 harder questions.\n"
          "Hard - 12 very hard questions.")
    difficulty = ("Choose difficulty(Easy/Normal/Hard) or write 'view' to view results \n"
                  "from previous games, or 'quit' to quit.")
    difficulty_choice = get_answer(difficulty, 'Choice: ', ['easy', 'normal', 'hard','view', 'quit']).lower()
    if difficulty_choice == 'easy':
        print("You chose 'Easy' difficulty. Let's begin!")
        play_easy()
    if difficulty_choice == 'normal':
        print("You chose 'Normal' difficulty. Let's begin!")
        play_normal()

    elif difficulty_choice == 'hard':
        print("You chose 'Hard' difficulty. Let's begin!")
        play_hard()

    elif difficulty_choice == 'view':
        mode = get_answer("Which difficulty's results do you want to view? (easy/normal/hard)?",
                          "Choice: ", ["easy", "normal", "hard"]).lower()
        load_results(results_file, difficulty=mode)

    elif difficulty_choice == 'quit':
        print('I hope you enjoyed the quizz. Goodbye!')
        break