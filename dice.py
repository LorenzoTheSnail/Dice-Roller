import random

while 5 < 7:
    
    ask = input('Do you want to roll the dice? Y/N:')
    if ask == str('Y'):
        x = random.randint(1,6)
        print(x)
    elif ask == str('N'):
        print('Okay then.')
        break
    else:
        print('Please answer with a capital Y or a Capital N.')
   