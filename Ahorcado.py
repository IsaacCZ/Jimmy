import random
import time

pictures = [
"""
 +----+
 |    |
      |
      |
      |
      |
======= """,
"""
 +----+
 |    |
 0    |
      |
      |
      |
======= """,

"""
 +----+
 |    |
 0    |
 |    |
      |
      |
======= """,

"""
 +----+
 |    |
 0    |
/|    |
      |
      |
======= """,

"""
 +----+
 |    |
 0    |
/|\   |
      |
      |
======= """,

"""
 +----+
 |    |
 0    |
/|\   |
/     |
      |
======= """,

"""
 +----+
 |    |
 0    |
/|\   |
/     |
      |
======= """,

"""
 +----+
 |    |
 0    |
/|\   |
/ \   |
      |
======= """,

]


words = ["dance", "eat", "aten","drink","drunk","deer"]
letterslist = ["a","b","c","d","e","f","g","h","i","j","k","l",
           "m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
mistakes = 0
correct = 0
attemps = 0
secret = []
mistakesList = []

def beginning():
    print("Let´s play a game, guess my word")
    

def wordChooser(words):
    index1 = random.randint(0,len(words)-1)
    return words[index1]

def board(word,mistakes):
    print(pictures[mistakes])
    print(f'This word has {len(word)} letters')


def tryit():
    global correct
    global attemps
    global mistakes
    global mistakesList
    global secret
    print("Give me a letter")
    letter = str(input()).lower()

    while letter not in letterslist:
        print("Give me a letter")
        letter = str(input()).lower()

    while letter in secret:
        print("You've chosen this letter before")
        letter = str(input()).lower()

    while letter in mistakesList:
        print("You've chosen this letter before and it's not in the my word")
        print("Give me a letter")
        letter = str(input()).lower()


        
    if letter in word:
        correct += 1
        attemps += 1
        secret.append(letter)
        secret = sorted(secret, key = lambda x: word.index(x))
        print(f'You have {correct} correct in {attemps} attemps')
        print(secret)
        print(f'Your fail attemps{mistakesList}')

            
    else:
        print(f'You have {mistakes} mistakes in {attemps} attemps')
        mistakes += 1
        attemps  += 1
        secret = sorted(secret, key = lambda x: word.index(x))
        mistakesList.append(letter)
        print(secret)
        print(f'Your fail attemps{mistakesList}')


def othergame():
    answers  = ["y", "n"]
    other = []

    while other not in answers:
        print("Do you want to play again | answer : 'y' or 'n'")
        other = str(input()).lower()

    if other == "y":
        return True
    else:
        return False
        
def wonlose():
    if set(word) == set(secret):
        print(f'You win, my word was {word}')
        othergame()
        return True
    
    else:
        return False


word = list(wordChooser(words))
game = True
won = False
###########
beginning()


while game == True:
    board(word,mistakes)
    tryit()

    if mistakes >= len(pictures)-1:
        print("You lose!!!")
        word = list(wordChooser(words))
        mistakes = 0
        correct = 0
        attemps = 0
        secret = []
        mistakesList = []
        game = othergame()

    won = wonlose()
    if won == True:
        word = list(wordChooser(words))
        mistakes = 0
        correct = 0
        attemps = 0
        secret = []
        mistakesList = []
        
    
    

    
