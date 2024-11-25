lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
p = x = y = 0
for c in range(8):
    lista[x][y] = (int(input(f'Digite [{x}, {y}]: ')))
    if y <= 1:
        y += 1
    else:
        y = 0
        x += 1
x = y = 0
for c in range(8):
    print(f'[{lista[x][y]:^5}]', end='   ')
    if y <= 1:
        y += 1
    else:
        y = 0
        x += 1
        print()
        print()
