import random
import os
from database import accounts
from art import logo,vs


def presenting_information(x):
    account = accounts[x]
    print(account['name'],', a',account['description'],', from',account['country'])
def fact_checking(a,b,choice):
    if (a < b and choice == 'a') or (a > b and choice == 'b'):
        os.system('cls')
        print('CORRECT!!!')
    else:
        os.system('cls')
        print(logo)
        print("WRONG! YOU LOSE!!!!! FINAL SCORE:",driver)
        exit()

m_words = ('y','n')
c_words = ('a','b')
driver = 0

while driver == 0:
    l_word = input("Press 'y' to play game or 'n' to exit:\n ")
    if l_word not in m_words:
        print("Please type 'y' or 'n'.")
        continue
    elif l_word  == 'n': exit()
    print(logo)
    while True:
        a = random.randint(0,49)
        b = random.randint(0,49)
        if a != b: break
    presenting_information(a)
    print(vs)
    presenting_information(b)
    while True:
        choice =input("Who has more followers? Is it 'a' or 'b'?\n")
        if choice not in c_words:
            print("Please type 'a' or 'b'!")
            continue
        else:
            fact_checking(a,b,choice)
            driver = driver + 1
            break
while driver > 0:
        a = b
        print('SCORE:',driver)
        while True and choice in c_words:
            b = random.randint(0,49)
            if a != b: break # ΩΣΤΕ ΝΑ ΜΗΝ ΤΑΥΤΙΖΩΝΤΑΙ ΟΙ ΔΥΟ ΕΠΙΛΟΓΕΣ!
        os.system('cls') 
        print(logo)
        presenting_information(a)
        print(vs)
        presenting_information(b)
        while True:
            choice =input("Who has more followers? Is it 'a' or 'b'?\n")
            if choice not in c_words:
                print("Please type 'a' or 'b'!")
                continue
            else:
                fact_checking(a,b,choice)
                driver = driver + 1 
            break

# ΔΕΝ ΜΠΟΡΩ ΝΑ ΚΑΝΩ ΤΟ ΠΑΙΧΝΙΔΙ ΝΑ ΞΑΝΑΠΑΙΖΕΙ ΑΥΤΟΜΑΤΑ ΧΩΡΙΣ ΝΑ ΠΑΤΗΣΩ ΤΟ PLAY ΑΠΟ ΤΗΝ ΕΦΑΡΜΟΓΗ ΚΑΙ ΕΝΩ ΠΑΡΑΛΛΗΛΑ ΠΡΙΝ ΣΥΜΒΕΙ ΑΥΤΟ ΝΑ ΚΑΘΑΡΗΣΩ ΤΟ ΠΕΡΙΕΧΟΜΕΝΟ ΣΤΟ TERMINAL 
# ΧΡΗΣΙΜΟΠΟΙΩΝΤΑΣ ΤΑ:
# import os 
# os.system('cls') 