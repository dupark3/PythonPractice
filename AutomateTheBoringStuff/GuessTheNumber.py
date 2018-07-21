import random

def game():
    print('I am thinking of a number between 1 and 20.')
    answer = random.randint(1,20)
    number = 0
    for i in range(6):
        print('Take a guess: ', end='')
        number = int(input())
        if number < answer:
            print('Your guess is too low.')
        elif number > answer:
            print('Your guess is too high.')
        else:
            break;
            
    if number == answer:
        print('Correct! You win.')
    else:
        print('You lose. The number I was thinking of was ' + str(answer))

game()