homens = mulheres20 = maioridade = 0
while True:
    print('...........Novo Cadastro............')
    try:
        idade = int(input('Idade: '))
    except:
        continue
    sexo = ' '
    while sexo not in 'FM':
        try:
            sexo = input('Sexo: ').strip().upper()[0]
        except:
            continue
    if idade > 18:
        maioridade += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres20 += 1
    print('Cadastro realizado com sucesso')
    print('-='*15)
    op = ' '
    while op not in 'SN':
        try:
            op = input('Que continuar? [S/N] ? ').strip().upper()[0]
        except:
            continue
    if op == 'N':
        break
print(f'Foram cadastrados {maioridade} pessoas com mais de 18 anos.\n{homens} Homens.\nE {mulheres20} mulheres com menos de 20 anos.')
