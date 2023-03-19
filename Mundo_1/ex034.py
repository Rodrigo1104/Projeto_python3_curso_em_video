s = float(input('Qual seu salario? R$: '))
if s > 1250:
    s = s * 1.10
else:
    s = s * 1.15
print(f'Seu novo saãrio é R${s:_.2f}'.replace('.', ',').replace('_', '.'))
