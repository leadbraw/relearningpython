import random

def drawBoard(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    if letter == 'X':
        return['X', 'O']
    else:
        return['O', 'X']
    
def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'
    
def playAgain():
    print('DO you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    return((bo[7] == le and bo[8] == le and bo[9] == le)
           or (bo[4] == le and bo[5] == le and bo[6] == le)
           or (bo[1] == le and bo[2] == le and bo[3] == le)
           or (bo[7] == le and bo[4] == le and bo[1] == le)
           or (bo[8] == le and bo[5] == le and bo[2] == le)
           or (bo[9] == le and bo[6] == le and bo[3] == le)
           or (bo[7] == le and bo[5] == le and bo[3] == le)
           or (bo[9] == le and bo[5] == le and bo[1] == le))

def getBoardCopy(board):
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)

    return dupeBoard
