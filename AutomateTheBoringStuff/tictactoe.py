import random
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['bot-L'] + '|' + board['bot-M'] + '|' + board['bot-R'])


def checkWin(board):
    if board['top-L'] != ' ' and \
       (board['top-L'] == board['top-M'] == board['top-R'] or \
        board['top-L'] == board['mid-L'] == board['bot-L']):
        print('Player ' + board['top-L'] + ' won!')
        return True

    if board['bot-R'] != ' ' and \
       (board['bot-R'] == board['bot-M'] == board['bot-L'] or \
        board['bot-R'] == board['mid-R'] == board['top-R']):
        print('Player ' + board['bot-R'] + ' won!')
        return True
    if board['mid-M'] != ' ' and \
       (board['mid-M'] == board['top-M'] == board['bot-M'] or \
        board['mid-M'] == board['mid-L'] == board['mid-R'] or \
        board['mid-M'] == board['top-L'] == board['bot-R'] or \
        board['mid-M'] == board['top-R'] == board['bot-L']):
        print('Player ' + board['mid-M'] + ' won!')
        return True
    return False


board = {'top-L' : ' ', 'top-M' : ' ', 'top-R' : ' ',
         'mid-L' : ' ', 'mid-M' : ' ', 'mid-R' : ' ',
         'bot-L' : ' ', 'bot-M' : ' ', 'bot-R' : ' '}

turn = random.choice(['X', 'O'])
printBoard(board)
while not checkWin(board):
    print('Player ' + turn + '\'s turn: ')    
    position = input()
    if board.get(position, 'Invalid') == ' ':
        board[position] = turn
    else:
        print('That position is invalid')
    printBoard(board)

    if turn == 'X':
        turn = 'O'
    else: 
        turn = 'X'
