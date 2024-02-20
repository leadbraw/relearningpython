import random
HANGMANPICS: str = ['''
               
    +---+
    |   |
        |
        |
        |
        |
    =========''', '''
    
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''
    
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''
    
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========''','''
    
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========''','''
    
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========''','''
    
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========''']

words = '''and baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog
donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse
mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat'''.split()

def getRandomWord(wordList: list) -> str:
    wordIndex: int = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(HANGMANPICS: list, missedLetters: str, correctLetters: str, secretWord: str):
    print(HANGMANPICS[len(missedLetters)])
    print()
    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks: str = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]
    for letter in blanks:
        print(letter, end= ' ')
    print()

def getGuess(alreadyGuessed: str) -> str:
    while True:
        print('Guess a letter')
        guess: str = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess
        
def playAgain() -> str:
    print('Do you want to play the game again? (yes or no)')
    return input().lower().startswith('y')

print('H A N G M A N !')
missedLetters: str = ''
correctLetters: str = ''
secretWord: str = getRandomWord(words)
gameIsDone: bool = False

while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
    guess: str = getGuess(missedLetters + correctLetters)
    if guess in secretWord:
        correctLetters = correctLetters + guess
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print(f'Yes! The secret word is {secretWord}! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print(f'You have run out of guesses!\nAfter {str(len(missedLetters))} missed guesses', 
                  f'and {str(len(correctLetters))} correct guesses, the word was "{secretWord}"')
            gameIsDone = True
    
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
    