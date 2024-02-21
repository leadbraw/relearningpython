import random

def drawBoard(board) -> None:
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

def inputPlayerLetter() -> list:
    letter: str = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    if letter == 'X':
        return['X', 'O']
    else:
        return['O', 'X']
    
def whoGoesFirst() -> str:
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'
    
def playAgain() -> bool:
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board: list[str], letter: str, move: int) -> None:
    board[move] = letter

def isWinner(bo, le) -> bool:
    return((bo[7] == le and bo[8] == le and bo[9] == le)
           or (bo[4] == le and bo[5] == le and bo[6] == le)
           or (bo[1] == le and bo[2] == le and bo[3] == le)
           or (bo[7] == le and bo[4] == le and bo[1] == le)
           or (bo[8] == le and bo[5] == le and bo[2] == le)
           or (bo[9] == le and bo[6] == le and bo[3] == le)
           or (bo[7] == le and bo[5] == le and bo[3] == le)
           or (bo[9] == le and bo[5] == le and bo[1] == le))

def getBoardCopy(board: list[str]) -> list[str]:
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpaceFree(board: list[str], move: int) -> bool:
    return board[move] == ' '

def getPlayerMove(board) -> int:
    move: str = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board: list[str], movesList: list[int]) -> int | None:
    possibleMoves: list = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
    
def getComputerMove(board: list[str], computerLetter: str) -> int:
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    if isSpaceFree(board, 5):
        return 5
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board) -> bool:
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

print('Welcome to Tic-Tac-Toe!')

while True:
    theBoard: list[str] = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn: str = whoGoesFirst()
    print(f'The {turn} turn will go first.')
    gameIsPlaying: bool = True

    while gameIsPlaying:
        if turn == 'player':
            drawBoard(theBoard)
            move: int = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'
        else:
            move: int = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'
    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break