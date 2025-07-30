import random

tools = ('rock','paper','scissors')
comp = tools[random.randint(0,2)]
type = input('ROCK,PAPER OR SCISSORS?')
choice = type.lower()

if choice not in tools:
    print('INVALID INPUT')
else :
    print(f'YOU: {choice}')
    print(f'COMPUTER: {comp}')
    if comp == choice:
        print('DRAW')
    elif (comp == 'rock' and choice == 'paper') or (comp == 'paper' and choice == 'scissors') or (comp == 'scissors' and choice == 'rock'):
        print('YOU WIN')
    else:
        print('YOU LOSE') 