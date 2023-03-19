print('[---------- Goliath National Bank ------------]')
sac = float(input('Quanto gostaria de sacar? R$ '))
nota_atual = 50
notas = 0
while True:
    if sac >= nota_atual:
        sac -= nota_atual
        notas += 1
    if sac < nota_atual:
        if notas > 0:
            print(f'{notas} notas de {nota_atual}')
        notas = 0
        if nota_atual == 50:
            nota_atual = 20
        elif nota_atual == 20:
            nota_atual = 10
        elif nota_atual == 10:
            nota_atual = 1
    if sac == 0:
        break
print('Foi entregue...')
