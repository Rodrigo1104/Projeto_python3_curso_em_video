from random import randint
from time import sleep
contador = 0
cont_list = 0
rep = []
jogos = []
descarte = []
n = 10 #int(input('Quantos jogos serão gerados: '))
for p in range(n):
    descarte.clear()
    while len(descarte) < 6:
        n = randint(1, 60)
        if n in descarte:
            contador += 1
            print(f'Aqui foi gerado  o {contador}ª numero repetido {n}, ')
        if n not in descarte:
            descarte.append(n)
            print(descarte)
    jogos.append(descarte[:])

print("\n\n\n\n*/*/*/*/*/*/*/* 30")
for c in jogos:
    print(sorted(c))
    sleep(1)
