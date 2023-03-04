from random import randint
from time import sleep
m = randint(1, 10)
j = 0
c = 0
print('what number did the machine choose from [1 to 10]')
while m != j:
    c += 1
    j = int(input('Number = '))
    print('Analyzing...', end='')
    sleep(1)
    if m != j:
        print('\033[31mSorry try again!!!\033[m')
    if m == j:
        print(f'\033[32mWinner {c}ª turn')
