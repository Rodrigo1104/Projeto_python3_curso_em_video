lista = (int(input('Digite 1ª Numero: ')), int(input('Digite 2ª Numero: ')), int(input('Digite 3ª Numero: ')), int(input('Digite 4ª Numero: ')))
print(f'Voce digitou os Numeros {lista}')
print(f'O valor 9 foi digitado {lista.count(9)} vezes')
if 3 in lista:
    print(f'O valor 3 apareceu na {lista.index(3) + 1}º posição')
else:
    print('O valor 3 nao foi digitado em nem uma posição')
print('os Valores pares digitados foram ', end='')
for par in lista:
    if par % 2 == 0:
        print(par, end=' ')