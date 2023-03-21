contagem = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte',)
R = int(input('Digite um Numero entre 0 e 20: '))
while True:
    if R > 20 or R < 0:
        R = int(input('Tente novamente...Digite um Numero entre 0 e 20: '))
    else:
        break
print(f'Voce digitou o numero {contagem[R]}')

