jogador = {'nome': input('Nome do jogador')}
gols = []
t = 0
p = int(input(f'quantas partidas o jogador {jogador['nome']} Jogou'))
for c in range(p):
    gp = int(input(f'Gols na {c + 1}ª Partida:  '))
    gols.append(gp)
    t += gp
jogador['gols'] = gols
jogador['total'] = t
print('=-'*30)
print(jogador)
print('=-' * 30)
for k, v in jogador.items():
    print(f'{k} tem valor {v}')
print('=-'*30)
print(f'O jogador {jogador['nome']} jogou {p} partidas')
for c in gols:
    print(f'==>> Na partida {c} ele fez {gols[c]} Gols.')


