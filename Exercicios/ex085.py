lista = [[], []]
for c in range(1, 8):
    v = int(input(f'digite o {c}ª Valor: '))
    if v % 2 == 0:
        lista[0].append(v)
    else:
        lista[1].append(v)


print(f'Lista de números pares {sorted(lista[0])}')
print(f'Lista de números pares {sorted(lista[1])}')
