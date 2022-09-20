c = 1
s = 0
n = 0
R = ''
while R != 'N':
    n = float(input(f'{c}ª Number = '))
    print(f'[{n}] Registered... ')
    print('=-'*15)
    c += 1
    s += n
    R = input('[N] to EXIT\n[Enter] New value        ').upper()
    print('=-' * 15)
print(f'Registered {c - 1} numbers\nSun of the Number is = {s}')
