s_years = 0
U_years = 0
U_years_name = ''
S_F_d2 = 0
for p in range(0, 4):
    name = input('')
    years = int(input(''))
    genre = input('').strip()
    print('='*10)
    s_years = s_years + years
    if p == 1 and genre in 'Mm':
        U_years = years
        U_years_name = name
    if genre in 'Mm' and years > U_years:
        U_years = years
        U_years_name = name
    if years < 20 and genre in 'Ff':
        S_F_d2 += + 1
print(f'''
Media is {s_years / 4}
Large years is {U_years_name}
down 20 female {S_F_d2}
''')
