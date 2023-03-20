from random import randint

n = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os numeros sorteados forão: ', end='')
for e in n:
    print(f'{e}', end=' ')
print(f'\nO maior numero foi: {max(n)}')
print(f'O menor numero foi: {min(n)}')
