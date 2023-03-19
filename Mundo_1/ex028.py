from random import randint
from time import sleep
c = randint(1, 3)
print('==='*10)
print('=      guess the number      ='.upper())
print('==='*10)
j = int(input('A number from 1 to 3: '))
print('')
print('processing...')
print('')
sleep(3)
if c == j:
    print('Congratulations you got it right')
else:
    print(f'The correct number was {c}, not {j}')
    print('Try again, you lost!')
