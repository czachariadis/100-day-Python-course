import random
from art import logo


pattern = "[a-z,A-Z]+"
m_words = ('y','n')
d_words = ('e','h','n')
LUCKY_NUM = random.randint(1,100)
i = 0

def num_guessing(gnum):
    if gnum == LUCKY_NUM:
        print("***YOU'RE RIGHT! YOU WON!***")
        exit()
    elif gnum < LUCKY_NUM:
        print("NOT QUITE.YOU'RE BELOW.")
    else:
        print("NOT QUITE.YOU'RE ABOVE.")

while True:
    l_word = input("Press 'y' to play game or 'n' to exit:\n ")
    if l_word not in m_words:
         print("Please type 'y' or 'n'.")
         continue
    elif l_word  == 'n': exit()
    print(logo)
    print("I'm picking a number between 1 and 100.Can you find it???")
    while True:
        diff = input("Press 'e' for EASY mode,'h' for HARD mode or 'n' to EXIT.\n")
        if diff not in d_words:
            print("Please type 'e','h' or 'n'")
            continue
        while diff in d_words:
            if diff == 'n': exit()
            elif diff == 'e':
                while i < 10:
                    try:
                        gnum = int(input("Guess the number:\n"))
                    except:
                        print("Please type numerical characters!")
                        continue
                    num_guessing(gnum)
                    i = i + 1
                    print('REMAINING GUESSES:',10-i)
                print("YOU'RE OUT OF GUESSES.YOU LOSE")
                print(f'Correct number: {LUCKY_NUM}')
                exit()
            else:
                while i < 5:
# ΠΡΟΤΙΜΑΜΕ while loops ΔΙΟΤΙ ΣΤΑ for i in range(5) loops Η ΜΕΤΑΒΛΗΤΗ-ΟΔΗΓΟΣ i ΘΑ ΑΛΛΑΖΕΙ ΠΑΝΤΑ ΤΙΜΗ ΚΑΤΑ 1 ΠΕΡΙΣΣΟΤΕΡΟ! 
                    try:
                        gnum = int(input("Guess the number:\n"))
                    except:
                        print("Please type numerical characters!")
                        continue
                    i = i + 1 
                    num_guessing(gnum)
                    print('REMAINING GUESSES:',5-i)
                print("YOU'RE OUT OF GUESSES.YOU LOSE")
                print(f'Correct number: {LUCKY_NUM}')
                exit()