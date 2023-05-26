lista_numeros = []
r = ''
print('=' * 30)
while True:
    try:
        novo_valor = int(input('Digite um valor: '))
    except:
        print('\033[1;31mDigite um numero valido\033[0;0m')
        continue
    if novo_valor not in lista_numeros:
        lista_numeros.append(novo_valor)
        print(f'\033[0;32mO numero {novo_valor} foi adicionado a lista...\033[0;0m')
    else:
        print(f'\033[1;31mO valor {novo_valor} não foi adicoonado pois Ja existe na na lista...\033[0;0m')
    try:
        r = input('Que continuar [S/N]: ').upper()[0]
    except:
        r = 'S'
    if r == 'N':
        break
    print('=' * 30)
print(f'Voce digitou os valores {sorted(lista_numeros)}')
