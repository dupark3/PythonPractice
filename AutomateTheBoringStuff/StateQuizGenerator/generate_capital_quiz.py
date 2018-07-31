#! /usr/bin/python3.5

import state_capitals, random, os

if not os.path.isdir('./Quizzes'):
    os.makedirs('./Quizzes')
if not os.path.isdir('./AnswerKeys'):
    os.makedirs('./AnswerKeys')

number_to_alpha = {0:'A', 1:'B', 2:'C', 3:'D'}

# Create 35 quizzes through the outer loop
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

    # Write header on the quiz
    quiz.write('Name: \nDate: \n\
                \tState Capitals Quiz (Form ' + quiz_number_string + ')\n\n')

    # Create 50 questions with 4 multiple choice options for each question
    for i in range(50):
        # Four random capitals. If correct answer already there, simply obtain its key.
        # If correct answer not there yet, overwrite a random position. 
        choices = random.sample(list(state_capitals.capitals.values()), 4)
        if state_capitals.capitals[states[i]] in choices:
            answer_number = choices.index(state_capitals.capitals[states[i]])
        else:
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
