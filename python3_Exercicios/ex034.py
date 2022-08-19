s = float(input('what is your salary? R$: '))
if s > 1250:
    s = s * 1.10
else:
    s = s * 1.15
print(f'You new salary is R${s:_.2f}'.replace('.', ',').replace('_', '.'))
