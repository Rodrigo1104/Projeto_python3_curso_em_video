import random
import emoji
from time import sleep
name = input('your Name? ')
w = ''
stone = emoji.emojize(":pedra:", language="pt")
paper = emoji.emojize(":rolo_de_papel:", language="pt")
scissors = emoji.emojize(":tesoura:", language="pt")
print(f'''=-=-=-=-=-=-=-=-=-=
rock Paper Scissors
=-=-=-=-=-=-=-=-=-=
[1]  {stone}   Stone 
[2]  {paper}   Paper
[3]  {scissors} Scissors
-=-=-=-=-=-=-=-=-=-=''')
a = int(input('Choice [?] '))
sleep(0.5)
print('Jo')
sleep(0.5)
print('Ken')
sleep(0.5)
print('Po...!')
sleep(2)
if a == 1:
    a = stone
elif a == 2:
    a = paper
elif a == 3:
    a = scissors
b = random.choice([stone, paper, scissors])
if a == b:
    w = 'ep'
elif (a == stone) and (b == paper):
    w = b
    v = 'Machine'
elif (a == stone) and (b == scissors):
    w = a
    v = name
elif (a == paper) and (b == stone):
    w = a
    v = name
elif (a == paper) and (b == scissors):
    w = b
    v = 'Machine'
elif (a == scissors) and (b == stone):
    w = b
    v = 'Machine'
elif (a == scissors) and (b == paper):
    w = a
    v = name
print(f'''\033[032m {name}\033[m: {a} x \033[031mmachine\033[m: {b} 
Winner : {w}''')
if w == a:
    print('\033[032m you won')
elif w == 'ep':
    print('\033[033mA Tie')
else:
    print('\033[031m      you lost')
