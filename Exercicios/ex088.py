from random import randint
from time import sleep
jogos = []
descarte = []
n = int(input('Quantos jogos serão gerados: '))
n2 = n
for p in range(n):
    descarte.clear()
    while len(descarte) < 6:
        n = randint(1, 60)
        if n not in descarte:
            descarte.append(n)
    jogos.append(descarte[:])

print(f'Gerando {n2} jogos...\n')
sleep(3)
for c in jogos:
    print(sorted(c))
    sleep(1)
print('\n Muito obrigado por utilizar nosso gerador de apostas, fique bem e volte sempre que precisar.')
