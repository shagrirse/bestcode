import random

cred = 100
oddeven = str(input('Odd/Even?: '))
betamt = int(input('How much would you like to bet?: '))
game = True

while game:
    number = random.randint(0,10)
    print(number)
    if cred > 0:
        if oddeven == 'Odd' and (number%2 > 0):
            print('Round Lost')
            cred = cred - betamt
        elif oddeven == 'Even' and (number%2 == 0):
            print('Round Won')
            cred = cred + betamt
    if cred <= 0:
        break