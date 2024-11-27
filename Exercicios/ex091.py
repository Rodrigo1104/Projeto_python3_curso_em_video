from random import randint
jogadores = {}
for c in range(1, 5):
    jogadores[f'Jogador {c}'] = randint(1, 6)
    print(f'O jogador {c} tirou {jogadores[f"Jogador {c}"]} no dado')

rank = dict(sorted(jogadores.items(), key=lambda item: item[1], reverse=True))
print('=-'*30)

for c, (k, v) in enumerate(rank.items()):
    print(f'{c+1}º lugar: {k} com {v}')
