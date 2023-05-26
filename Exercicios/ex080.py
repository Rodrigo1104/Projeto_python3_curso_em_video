lista_numero = []
for numero in range(0, 5):
    n = int(input('Digite um valor: '))
    if numero == 0 or n > lista_numero[-1]:
        lista_numero.append(n)
    else:
        pos = 0
        while pos < len(lista_numero):
            if n <= lista_numero[pos]:
                lista_numero.insert(pos, n)
                print(f'{n} foi adicionado na posição {pos}')
                break
            pos += 1
print(sorted(lista_numero))
