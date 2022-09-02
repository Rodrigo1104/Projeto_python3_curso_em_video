from datetime import date
at = date.today().year
ano = int(input('ano nascimento'))
sexo = input('SEXO ? M/F').upper()
idade = at - ano
if idade < 18 and sexo == 'M':
    f = 18 - idade
    dal = ano + 18
    print(f'''voce nasceu em {ano} e tem {idade} em 2022.
ainda falta {f} para o alistamento
seu alistamento sera em {dal}''')
elif idade > 18 and sexo == 'M' or sexo == 'm':
    p = idade - 18
    dal = ano + 18
    print(f'''voce nasceu em {ano} e tem {idade} em 2022.
    voce ja deveria ter se alistado a {p} anos.
    seu alistamento foi em  {dal}''')
elif idade == 18 and sexo == 'M':
    print(f'''voce nasceu em {ano} e tem {idade} em 2022.
    vc tem que se alistar IMEDIATAMENTE''')
elif sexo == 'F':
    print('Vc não precisa se alistar')
else:
    print('Digite f ou F para feminino M ou m para masculino ')
