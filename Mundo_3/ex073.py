brasileirao = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians',
               'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza',
               'São Paulo', 'Botafogo', 'América-MG', 'Santos', 'Goiás',
               'Red Bull Bragantino', 'Coritiba', 'Cuiabá', 'Ceará',
               'Atlético-GO', 'Avaí', 'Juventude')
print('====================================')
print(f'Lista de times do Brasileirão : {brasileirao}')
print('====================================')
print(f'Os 5 primeiros são: {brasileirao[:5]}')
print('====================================')
print(f'Os 4 ultimos são: {brasileirao[-4:]}')
print('====================================')
print(f'Times em ordem alfabetica: {sorted(brasileirao)}')
print('====================================')
print(f'O corithians esta na {brasileirao.index("Corinthians") + 1}ª Posição')
print('====================================')
