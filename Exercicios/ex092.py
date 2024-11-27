from datetime import date
data = date.today().year
dados = {'nome': input('Nome: '), 'idade': data - int(input('Ano de nascimento')), 'ctps': int(input('Numero da carteira de trabalho se houver: ')) or 0}

if dados['ctps'] != 0:
    dados['ano contrato'] = int(input('Ano de contratação'))
    dados['Salario'] = float(input('Salario'))
    dados['ano aposentadoria'] = dados['idade'] + (35 - (data - dados['ano contrato']))
print('=-'*30)
for k, v in dados.items():
    print(f'  -- {k} Tem o valor: {v}')
