matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]    # inicializando a matriz 3 x 3
sp = vc3 = mvl2 = 0
for col in range(3):    # Preenchendo a matriz com os valores fornecidos pelo user
    for lin in range(3):
        matriz[col][lin] = int(input(f'[{col},{lin}]: '))
        if matriz[col][lin] % 2 == 0:
            sp += matriz[col][lin]
        if lin == 2:
            vc3 += matriz[col][lin]
        if col == 1 and lin == 0:
            mvl2 = matriz[col][lin]
        if col == 1 and matriz[col][lin] > mvl2:
            mvl2 = matriz[col][lin]


# Mostrando a matriz ao usuário
for col in range(3):
    for lin in range(3):
        print(f'[{matriz[col][lin]:^5}]', end='')
    print('\n')

print(f'A soma de todos os valores pares digitados é: {sp}\n'
      f'A soma dos valores da terceira coluna é: {vc3}\n'
      f'O maior valor da segunda linha é: {mvl2}')
