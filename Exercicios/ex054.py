from datetime import date
U_years = 0
D_years = 0
for c in range(0, 7):
    Years_old = date.today().year - int(input(''))
    if Years_old >= 21:
        U_years += + 1
    if Years_old < 21:
        D_years += + 1
    print(f'{Years_old}')
print(f'{U_years} {D_years}')
