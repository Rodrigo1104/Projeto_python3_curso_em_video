from random import randint
c = 0
print('VAMOS JOGAR PAR OU ÍMPAR')
while True:
    jogador = int(input('Escolha um Valor: '))
    maquina = randint(0, 10)
    s = jogador + maquina
    op = ' '
    while op not in 'PpIi':
        op = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    if (s % 2) == 0:
        r = 'P'
        r1 = 'Par'
    else:
        r = 'I'
        r1 = 'Ímpar'
    print(f'Voce jogou {jogador} e o computador {maquina}. total de {s} deu {r1} ')
    print('--' * 20)
    if op != r:
        break
    print('Voçê VENCEU!')
    print('Vamos jogar novamente...')
    print('--'*20)
    c += 1
print(f'GAMER OVER! Voçê venceu {c} vezes.')
