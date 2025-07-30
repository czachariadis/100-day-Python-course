from art_on_blackjack import logo
import random

cards = (11,2,3,4,5,6,7,8,9,10,10,10,10)
m_words = ('y','n') 
player = []
dealer = []
p_score = 0
d_score = 0
def dealer_cards():
    print("Dealer's cards:",dealer)
    print(f"Dealer's score: {d_score}")
while True:
    game_cont = input("If you want to play blackjack press 'y' or press 'n' to exit\n")
    if game_cont not in m_words:
        print('*Invalid answer.*')
    elif game_cont == 'n':
        break
    else:
        print(logo)
        for i in range(2):
            random_card = cards[random.randint(0,12)]
            player.append(random_card)
            p_score =+ sum(player)        
        print(player)
        print('Your score:',p_score)
        while (d_score < 17):
            random_card = cards[random.randint(0,12)]
            dealer.append(random_card)
            d_score =+ sum(dealer)
            if d_score > 21 and cards[0] in dealer:
                cards[0] == 1
        print("Dealer's first card:",dealer[0])
        card_drawer = input("If you want to draw another card press 'y' or else press 'n'\n")
        if card_drawer not in m_words:
            print('*Invalid answer.*')
        elif card_drawer == 'n':
            break
        else:
            random_card = cards[random.randint(0,12)]
            player.append(random_card)
            p_score =+ sum(player)
            print(player)
            print('Your score:',p_score)
            if p_score > 21 and cards[0] in player:
                cards[0] == 1
    if p_score > 21 :
        print('YOU WENT OVER.')
        break
if (p_score > d_score and p_score <= 21) or (p_score <= 21 and d_score > 21):
    print('YOU WON')
    dealer_cards()
else:
    print('YOU LOSE')
    dealer_cards()
# ΕΙΝΑΙ ΑΡΚΕΤΑ ΠΙΘΑΝΟ ΝΑ ΥΠΑΡΧΕΙ ΑΚΟΜΑ ΘΕΜΑ ΜΕ ΤΗΝ ΑΝΤΙΚΑΤΑΣΤΑΣΗ ΤΟΥ ΑΣΣΟΥ!!!!! ΕΠΙΣΗΣ ΕΜΦΑΝΙΖΕΙ ΠΕΡΙΟΔΙΚΑ BUGS.
# TODO- make it able to replace 11 to 1.