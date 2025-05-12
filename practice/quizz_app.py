import json

def get_answer(question_text, prompt, valid_choices):
    while True:
        print(question_text)
        answer = input(prompt)
        if answer not in valid_choices:
            print(f'Please enter a number between {valid_choices[0]} and {valid_choices[-1]}.')
        else:
            return answer


correct_easy = 0
correct_normal = 0
correct_hard = 0
incorrect_easy = 0
incorrect_normal = 0
incorrect_hard = 0

while True:
    print('Welcome to the Quizz. Please choose a difficulty level.\nEasy - 8 easy questions.\nNormal - 10 harder questions.\n'
          'Hard - 12 very hard questions.')
    difficulty = input('Choose difficulty(Easy/Normal/Hard): ').lower()

    if difficulty == 'easy':
        q_e_1 = ('What is the capital of Germany?:\n1.Munich\n2.Berlin\n3.Frankfurt am Main\n4.Hamburg')
        a_e_1 = get_answer(q_e_1, 'Answer(1-4): ', ['1', '2', '3', '4'])
        if a_e_1 == '2':
            correct_easy += 1
            print('right')
        else:
            incorrect_easy += 1
            print('wrong')
        q_e_2 = ('Who was chancellor of Germany during the Second World War?:\n'
                 '1.Angela Merkel\n2.Olaf Schulz\n3.Otto von Bismark\n4.Adolf Hitler')
        a_e_2 = get_answer(q_e_2,'Answer(1-4): ', ['1', '2', '3', '4'])
        if a_e_2 == '4':
            correct_easy += 1
        else:
            incorrect_easy += 1
        q_e_3 = ('Which were the two Major Powers opposing each other during the Cold War?:\n'
                 '1.USA/USSR\n2.Germany/Austria\n3.Italy/Spain\n4.North Africa/South Africa')
        a_e_3 = get_answer(q_e_3,'Answer(1-4): ', ['1', '2', '3', '4'])
        if a_e_3 == '1':
            correct_easy += 1
        else:
            incorrect_easy += 1
        q_e_4 = ('Which individual received most of the blame for the September 11th 2001 attack on the World Trade'
                 'Center?:\n1.Muammar Gaddafi\n2.Muhammad Ali\n3.Osama bin Laden\n4.Saddam Hussein')
        a_e_4 = get_answer(q_e_4,'Answer: ', ['1', '2', '3', '4'])
        if a_e_4 == '3':
            correct_easy += 1
        else:
            incorrect_easy += 1
        q_e_5 = ('Which system did the german philosopher Karl Marx write about for most of his life?:\n'
                 '1.Communism\n2.Egalitarianism\n3.Capitalism\n4.Windows XP')
        a_e_5 = get_answer(q_e_5, 'Answer: ', ['1', '2', '3', '4'])
        if a_e_5 == '3':
            correct_easy += 1
        else:
            incorrect_easy += 1
        q_e_6 = ('Who invented the iPhone?:\n1.Bill Gates\n2.Steve Jobs\n3.Scientists at Apple\n4.Jeff Bezos')
        a_e_6 = get_answer(q_e_6, 'Answer: ', ['1', '2', '3', '4'])
        if a_e_6 == '3':
            correct_easy += 1
        else:
            incorrect_easy += 1
        q_e_7 = ('Which country is the only country in the history of the world to use an atom bomb?:\n1.Russia\n'
                 '2.USA\n3.Germany\n4.UK')
        a_e_7 = get_answer(q_e_7, 'Answer: ', ['1', '2', '3', '4'])
        if a_e_7 == '2':
            correct_easy += 1
        else:
            incorrect_easy += 1
        q_e_8 = ('As of 2025, how many years has the US been engaged in a war with other countries or entities in the'
                 'world?:\n1.24\n2.7\n3.The US has not been at war recently\n4.12')
        a_e_8 = get_answer(q_e_8, 'Answer: ', ['1', '2', '3', '4'])
        if a_e_8 == '1':
            correct_easy += 1
        else:
            incorrect_easy += 1
        print(f'Congratulations! You made it until the end of the quizz!\nYou guessed {correct_easy} questions'
              f'correctly and {incorrect_easy} incorrectly!')
        if correct_easy == 8:
            print('Excellent! You got them all right!')
        elif correct_easy >= 5:
            print('Very good!')
        elif incorrect_easy == 8:
            print('You should learn some more.')
        else:
            print('Maybe you should try again.')