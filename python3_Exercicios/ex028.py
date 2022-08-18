from random import randint
n = randint(1, 5)
r = int(input('Number: '))
print(n, r, 'Congratulation, you won' if n == r else 'sorry the computer wow, try again')
