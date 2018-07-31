#! /usr/bin/python3.5

import state_capitals, random, os

if not os.path.isdir('./Quizzes'):
    os.makedirs('./Quizzes')
if not os.path.isdir('./AnswerKeys'):
    os.makedirs('./AnswerKeys')

number_to_alpha = {0:'A', 1:'B', 2:'C', 3:'D'}

for quiz_number in range(1,36):
    # Write quiz and answer key files with correct number
    if quiz_number < 10:
        quiz_number_string = '0' + str(quiz_number)
    else:
        quiz_number_string = str(quiz_number)
    quiz = open(os.path.join('./Quizzes/CapitalsQuizNumber' + quiz_number_string +'.txt'), 'w')
    answer_key = open(os.path.join('./AnswerKeys/AnswerKeyNumber' + quiz_number_string + '.txt'), 'w')
        
    # Shuffle state names
    states = list(state_capitals.capitals.keys())
    random.shuffle(states)

    for i in range(50):
        # Obtain four random choices of capitals, and overwrite one of them with answer
        choices = []
        for j in range(4):
            choices.append(random.choice(list(state_capitals.capitals.values())))
        answer_number = random.randint(0,3)
        choices[answer_number] = state_capitals.capitals[states[i]]
        
        # Write the state and the four choices and the answer
        quiz.write(str(i + 1) + '. Capital of ' + states[i] + ' is: \n' +
                   '    A. ' + choices[0] + '\n' + 
                   '    B. ' + choices[1] + '\n' +
                   '    C. ' + choices[2] + '\n' +
                   '    D. ' + choices[3] + '\n\n')
        answer_key.write(str(i + 1) + '. ' + number_to_alpha[answer_number] + '\n')
        
    quiz.close()
    answer_key.close()
