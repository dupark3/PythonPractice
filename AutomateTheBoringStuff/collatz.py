def collatz(number):
    if number == 1:
        return
    elif number % 2 == 0:
        number = number // 2
        print(number)
        collatz(number)
    else:
        number = number * 3 + 1
        print(number)
        collatz(number)

def game():
    try:
        print('Enter your number to call collatz seq on: ')
        number = int(input())
        collatz(number)
    except ValueError:
        print('Error: must enter an integer')

while(True):
    game()
    print('Play again? Type Yes or No')
    playAgain = input()
    if playAgain == 'No':
        break
    elif playAgain == 'Yes':
        continue
    else:
        print('Invalid response, ending game.')
        break
