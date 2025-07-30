from data import c_emoj,MENU,resources
import os
from decimal import Decimal,getcontext
 
m_words = ('e','l','c',"off","report")
coffe_d = {'e': "espresso",'l': "latte",'c': "cappuccino"}
money = 0
mon_values = {"quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}

# def changing(c_value,price,order):
#     try:
#         q = int(input("How many quarters?\n")) * 0.25
#         d = int(input("How many dimes?\n")) * 0.10
#         n = int(input("How many nickles?\n")) * 0.05
#         p = int(input("How many pennies?\n")) * 0.01
#     except:
#         print('WRONG INPUT')
#         return
#     c_value =+ p + q + d + n
#     if price > c_value:
#         print("SORRY YOU DONT HAVE ENOUGH MONEY...")
#     else:
# # **** ΜΕ ΑΥΤΗ ΤΗ ΜΕΘΟΔΟ ΔΕΝ ΕΜΦΑΝΙΖΩΝΤΑΙ ΠΕΡΙΕΡΓΑ ΑΠΟΤΕΛΕΣΜΑΤΑ ΣΤΙΣ ΠΡΑΞΕΙΣ ΔΕΚΑΔΙΚΩΝ ΑΡΙΘΜΩΝ ΛΟΓΩ ΤΗΣ PYTHON!!! ****
#         getcontext().prec = 2
#         change = Decimal(c_value) - Decimal(price)
#         print(f"GOOD. ENJOY YOUR {order.upper()} {c_emoj}. HERE IS YOUR {change} $ CHANGE...")
# # ΤΙΣ ΕΠΙΛΟΓΕΣ 'off' ΚΑΙ 'report' ΤΙΣ ΞΕΡΟΥΝ ΜΟΝΟ ΟΙ ΙΔΙΟΚΤΗΤΕΣ ΓΙΑ ΑΥΤΟ ΔΕΝ ΑΠΟΚΑΛΥΠΤΕΤΑΙ ΩΣ ΕΠΙΛΟΓΗ.
while True:
    ch = input(f"Choose your coffe {c_emoj}. Press 'e' for espresso, 'l' for latte or 'c' for cappuccino:\n")
    if ch not in m_words:
        print("WRONG INPUT")
        continue
    elif ch == "report":
        print("Water: ", resources["water"],"ml")
        print("Milk:",resources["milk"],"ml")
# TODO- (sp. ΝΑ ΒΡΕΙΣ ΤΡΟΠΟ ΝΑ ΕΜΦΑΝΙΖΟΝΤΑΙ ΑΥΤΟΜΑΤΑ ΟΙ ΜΟΝΑΔΕΣ ΜΕΤΡΗΣΗΣ ΑΝΑΛΟΓΑ ΜΕ ΤΟ ΥΛΙΚΟ.)
        print("Coffe: ", resources["coffee"],"g")
        print("Money: ", money,"$")
        continue
    elif ch == "off":
        os.system('cls')
        exit()
    order = coffe_d[ch]
    price = MENU[order]['cost']
    money =+ price
    while True:
        try:
            c_value = 0
            q = int(input("How many quarters?\n")) * 0.25
            break
        except:
            print('WRONG INPUT')
            continue
    while True:
        try:
            d = int(input("How many dimes?\n")) * 0.10
            break
        except:
            print('WRONG INPUT')
            continue
    while True:
        try:
            n = int(input("How many nickles?\n")) * 0.05
            break
        except:
            print('WRONG INPUT')
            continue
    while True:
        try:
            p = int(input("How many pennies?\n")) * 0.01
            break        
        except:
            print('WRONG INPUT')
            continue
    c_value =+ p + q + d + n
    if price > c_value:
        print("SORRY YOU DONT HAVE ENOUGH MONEY...")
        break
    else:
# **** ΜΕ ΑΥΤΗ ΤΗ ΜΕΘΟΔΟ ΔΕΝ ΕΜΦΑΝΙΖΩΝΤΑΙ ΠΕΡΙΕΡΓΑ ΑΠΟΤΕΛΕΣΜΑΤΑ ΣΤΙΣ ΠΡΑΞΕΙΣ ΔΕΚΑΔΙΚΩΝ ΑΡΙΘΜΩΝ ΛΟΓΩ ΤΗΣ PYTHON!!! ****
        getcontext().prec = 2
        change = Decimal(c_value) - Decimal(price)
        print(f"GOOD. ENJOY YOUR {order.upper()} {c_emoj}. HERE IS YOUR {change} $ CHANGE...")
# ingredients:
    ingr = MENU[order]['ingredients']
    for a,b in ingr.items():
        for c,d in resources.items():
            if d < 0:
                print(f"SORRY WE DONT HAVE ENOUGH {a.upper()}")
                break
            elif a == c:
                resources[a] = resources[a] - b
                continue
        break
# TODO - (sp. ΝΑ ΒΡΕΙΣ ΤΡΟΠΟ ΣΕ ΠΕΡΙΠΤΩΣΗ ΠΟΥ ΔΕΝ ΕΙΣΠΡΑΤΩΝΤΑΙ ΤΑ ΑΠΑΡΑΙΤΗΤΑ ΛΕΦΤΑ 'Η ΔΕΝ ΥΠΑΡΧΟΥΝ ΤΑ ΑΠΑΡΑΙΤΗΤΑ ΥΛΙΚΑ ΑΝΤΙ ΝΑ ΚΛΕΙΝΕΙ ΤΟ TERMINAL ΝΑ ΣΕ ΕΠΙΣΤΡΕΦΕΙ ΣΤΗΝ ΕΠΙΛΟΓΗ ΤΟΥ ΚΑΦΕ ΚΑΙ ΟΤΑΝ ΔΕΝ
# ΥΠΑΡΧΟΥΝ ΤΑ ΑΠΑΡΑΙΤΗΤΑ ΥΛΙΚΑ ΝΑ ΜΗΝ ΞΩΔΕΥΟΝΤΑΙ ΠΟΣΟΤΗΤΕΣ ΑΠΟ ΤΙΣ ΠΡΟΜΗΘΕΙΕΣ ΓΙΑ ΝΑ ΦΤΙΑΧΤΕΙ Ο ΑΠΛΗΡΩΤΟΣ ΚΑΦΕΣ!)