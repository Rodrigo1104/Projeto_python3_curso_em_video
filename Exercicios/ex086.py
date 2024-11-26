matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]    # inicializando a matriz 3 x 3

for col in range(3):    # Preenchendo a matriz com os valores fornecidos pelo user
    for lin in range(3):
        matriz[col][lin] = int(input(f'[{col},{lin}]: '))
for col in range(3):
    for lin in range(3):
        print(f'[{matriz[col][lin]:^5}]', end='')
    print('\n')
