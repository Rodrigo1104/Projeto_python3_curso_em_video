from random import randint
from time import sleep
m = randint(1, 10)
j = 0
c = 0
print('what number did the machine choose from [1 to 10]')
while m != j:
    c += 1
    j = int(input())
    print('Analyzing...')
    sleep(0.1)
    if m != j:
        print('Sorry try again!!!')
    if m == j:
        print(f'Winner {c}ª turn')
