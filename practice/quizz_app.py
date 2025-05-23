import json
import os
import random

from practice.questions import easy_questions, normal_questions, hard_questions, bonus_hard_question


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

with open("questions.json", "r", encoding="utf-8") as f:
    all_questions = json.load(f)


selected_easy = random.sample(all_questions["easy"], 8)
selected_normal = random.sample(all_questions["normal"], 10)
selected_hard = random.sample(all_questions["hard"], 12)
bonus_question = all_questions["bonus"]



def play_quiz(difficulty_name, selected_questions, is_bonus_available=False, bonus_question=None):
    correct = 0
    incorrect = 0
    results = []

    for q in selected_questions:
        formated = f"{q['question']}\n" + "\n".join(q['choices'])
        user_answer = get_answer(formated, "Answer(1-4): ", ["1", "2",
                                                             "3", "4", "quit"]).lower()
        if user_answer == "quit":
            print("Quiz exited. No results saved.")
            return
        is_correct = user_answer == q['answer']
        correct += int(is_correct)
        incorrect += int(not is_correct)
        results.append({
            "difficulty": difficulty_name,
            "question": q["question"],
            "choices": q["choices"],
            "your_answer": user_answer,
            "correct_answer": q["answer"],
            "is_correct": is_correct
        })

    if is_bonus_available and correct >= 7 and bonus_question:
        print("You have enough points to get a Bonus Question.")
        chance = get_answer("Would you like to try the Bonus Question?",
                            "Yes or No (y/n): ",["y", "n"])
        if chance == "y":
            for q in bonus_question:
                bonus_formated = f"{q['question']}\n" + "\n".join(q['choices'])
                bonus_user_answer = get_answer(bonus_formated, "Answer(1-4): ",
                                               ["1", "2", "3", "4"])
                is_correct_b = bonus_user_answer == q['answer']
                correct += int(is_correct_b)
                incorrect += int(not is_correct_b)
                results.append({
                    "difficulty": difficulty_name,
                    "question": q["question"],
                    "choices": q["choices"],
                    "your_answer": bonus_user_answer,
                    "correct_answer": q["answer"],
                    "is_correct": is_correct_b,
                    "is_bonus": True
                })
    elif is_bonus_available:
        print("You didn't get enough points to try the Bonus Question.")

    print(f"You got {correct} correct and {incorrect} incorrect.")

    if correct == len(selected_questions) + (1 if is_bonus_available and
                                                  correct > len(selected_questions) else 0):
        print("Excellent! You got them all right!")
    elif correct >= int(0.8 * len(selected_questions)):
        print("Very good!")
    elif correct >= int(0.5 * len(selected_questions)):
        print("Good.")
    elif correct >= 1:
        print("Maybe you should try again")
    else:
        print("You should learn more about the world.")

    save_results(results_file, results, difficulty=difficulty_name)


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
    if difficulty_choice == "easy":
        print("You chose 'Easy' difficulty. Let's begin!")
        play_quiz("easy", selected_easy)
    if difficulty_choice == "normal":
        print("You chose 'Normal' difficulty. Let's begin!")
        play_quiz("normal", selected_normal)

    elif difficulty_choice == "hard":
        print("You chose 'Hard' difficulty. Let's begin!")
        play_quiz("hard", selected_hard, is_bonus_available=True, bonus_question=bonus_hard_question)

    elif difficulty_choice == 'view':
        mode = get_answer("Which difficulty's results do you want to view? (easy/normal/hard)?",
                          "Choice: ", ["easy", "normal", "hard"]).lower()
        load_results(results_file, difficulty=mode)

    elif difficulty_choice == 'quit':
        print('I hope you enjoyed the quizz. Goodbye!')
        break