lista_descartavel = []
lista_mae = []
lista_Pesadao = []
lista_levinhos = []
maior = menor = 0
while True:
    lista_descartavel.append(str(input(f'Nome: ')))
    lista_descartavel.append(float(input(f'peso: ')))
    if len(lista_mae) == 0:
        menor = maior = lista_descartavel[1]
        lista_levinhos.append(lista_descartavel[:][0])
        lista_Pesadao.append(lista_descartavel[:][0])
    else:
        if lista_descartavel[1] == menor:
            lista_levinhos.append(lista_descartavel[:][0])
        if lista_descartavel[1] < menor:
            menor = lista_descartavel[1]
            lista_levinhos.clear()
            lista_levinhos.append(lista_descartavel[:][0])
        if lista_descartavel[1] == maior:
            lista_Pesadao.append(lista_descartavel[:][0])
        if lista_descartavel[1] > maior:
            maior = lista_descartavel[1]
            lista_Pesadao.clear()
            lista_Pesadao.append(lista_descartavel[:][0])
    lista_mae.append(lista_descartavel[:])
    lista_descartavel.clear()
    r = str(input('Continuar? [S/N]')).upper()[0]
    if r not in 'NS':
        while r not in 'NS':
            print('Opção invalida. digite apens [S] para sim ou [N] para não')
            r = str(input('Continuar? [S/N]')).upper()[0]
    if r == 'N':
        break
print(f'Lista das mais leves {menor} {lista_levinhos}')
print(f'Lista das mais pesadas {maior} {lista_Pesadao}')
print(f'{len(lista_mae)} Pessoas foram cadastradas')
