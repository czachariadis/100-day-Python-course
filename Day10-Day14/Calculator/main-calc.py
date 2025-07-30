from art_on_calculator import logo

# add 
def add(n1,n2):
    return n1 + n2
# substract
def substract(n1,n2):
    return n1 - n2
# multiply
def multiply(n1,n2):
    return n1 * n2
# divide
def divide(n1,n2):
    return n1 / n2 
operations = {'+': add,'-': substract,'*': multiply,'/': divide}
def calculator():
    print(logo)
    try:
        n1 = float(input("What's the first number?\n" ))
        for symbol in operations:
            print(symbol)
        operation_symbol = input('Pick an operation from above:')
        if operation_symbol not in operations:
            print('Wrong operations input')
        else:
            n2 = float(input("What's the second number?\n"))
            calc_f = operations.get(operation_symbol)
            answer = calc_f(n1,n2)
            print(f'{n1} {operation_symbol} {n2} = {answer}')
            clist = ('y','n')
            while True:
                choice = input("Pick 'y' to continue calculating or 'n' to exit:")
                if choice not in clist:
                    print('Invalid input')
                    continue
                elif choice == 'n':
                    break
                else:
                    next_op = input('Pick next operation:')
                    if next_op not in operations:
                        print('Wrong operations input')
                    else:
                        next_num = float(input("What's the next number?\n")) 
                        calc_f = operations.get(next_op)
                        answer = calc_f(answer,next_num)
                        print(answer)

    except:
        print('Please type numerical characters')
calculator()