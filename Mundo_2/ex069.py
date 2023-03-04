homens = mulheres20 = maioridade = 0
while True:
    try:
        idade = int(input('Idade: '))
    except:
        continue
    sexo = ' '
    while sexo not in 'FM':
        sexo = input('Sexo: ').strip().upper()[0]
    if idade > 18:
        maioridade += 1
    print('Cadastro realizado com sucesso')
    print('-='*15)
    op = ' '
    while op not in 'SN':
        op = input('Que continuar? [S/N] ? ').strip().upper()[0]
    if op == 'N':
        break
