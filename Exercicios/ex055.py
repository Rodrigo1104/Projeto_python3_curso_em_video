U_peso = 0
D_peso = 0
for c in range(0, 5):
    peso = float(input(''))
    if c == 1:
        U_peso = peso
        D_peso = peso
    if peso > U_peso:
        U_peso = peso
    if peso < D_peso:
        D_peso = peso
print(f'{U_peso} {D_peso}')

