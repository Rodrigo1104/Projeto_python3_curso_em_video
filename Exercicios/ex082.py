lista_numeros = []
lista_par = []
lista_impar = []
while True:
    lista_numeros.append(int(input('Digite um valor: ')))
    r = str(input('CONTINUE[S/N]')).upper()[0]
    if r in 'nN':
        break

for numero in lista_numeros:
    if numero % 2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)
print(f'A lista completa é: {sorted(lista_numeros)}')
print(f'A lista numeros pares é: {sorted(lista_par)}')
print(f'A lista dos numeros impares é: {sorted(lista_impar)}')
