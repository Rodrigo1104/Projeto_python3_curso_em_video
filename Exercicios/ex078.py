lista_numeros = []
maior = menor = ''
for numero in range(0, 5):
    lista_numeros.append(int(input(f'{numero + 1}ª numero: ')))
print(f'Os numeros digitados foram: {lista_numeros}')
print(f'O maior numero foi {max(lista_numeros)} ', end='nas posiçoes ')
for pos, numero in enumerate(lista_numeros):
    if max(lista_numeros) == numero:
        print(f'{pos}', end='...')
print(f'\nO menor numero foi {min(lista_numeros)} ', end='nas posiçoes ')
for pos, numero in enumerate(lista_numeros):
    if min(lista_numeros) == numero:
        print(f'{pos}', end='...')
