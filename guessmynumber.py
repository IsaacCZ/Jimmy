import random

def getnumber(numbersize):
    numbers = list(range(10))
    random.shuffle(numbers)
    secretnum = ''
                                    
    for i in range(numbersize):
        secretnum += str(numbers[i])
    return secretnum

def getclues(conjeture,secretnum):
    if conjeture == secretnum:
        return "You get it, You won!"
    
    clue = []

    for i in range(len(conjeture)):
        if conjeture[i] == secretnum[i]:
            clue.append('fermi')
        elif conjeture[i] in secretnum:
            clue.append('pico')
    if len(clue) == 0:
        return 'bagels'

    clue.sort()
    return ''.join(clue)

def isnumber(num):
    if num == '':
        return False

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False
    return True

def playagain():
    print("do you want to play again ? | 'y' or 'n' ")
    return input().lower().startswith('y')


#################

numbersize = 3
maxguess = 10

print("I'm thinking a %s digits number, guess it" %(numbersize))
print("Here you have some clues:")
print("bagels: None of the three digits guessed is in the secret number.")
print("pico: One of the digits is in the secret number, but the guess has the digit in the wrong place.")
print("fermi: The guess has a correct digit in the correct place.")

while True:
    secretnum = getnumber(numbersize)
    print(f"i've thougth a {numbersize} digits number, you have {maxguess} oportunites to guess it")
    attemps = 1
    print(secretnum)
    while attemps <= maxguess:
        conjeture = ''
        while len(conjeture) != numbersize or not isnumber(conjeture):
            print(f'conjeture number {attemps}')
            conjeture = input()

        clue = getclues(conjeture,secretnum)
        print(clue)
        attemps+=1

        if conjeture == secretnum:
            break
        if attemps > maxguess:
            print(f"You lose my number was{secretnum}")

    if not playagain():
        break
        
