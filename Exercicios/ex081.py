lista_numeros = []
while True:
    lista_numeros.append(int(input('Digite um valor: ')))
    r = str(input('CONTINUE[S/N]')).upper()[0]
    if r in 'nN':
        break

print(F'Foram digitados {len(lista_numeros)} numeros')
print(f'Os numeros em ordem decrescente {sorted(lista_numeros, reverse=True)}')
if 5 in lista_numeros:
    print('O numero 5 esta na lista')
else:
    print('O numero 5 nao esta na lista')
