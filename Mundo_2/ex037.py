n = int(input('Number? :'))
print('''CONVERTING
[1] Binario
[2] Octal
[3]Hexadecimal''')
r = (int(input('')))
if (r > 3) or (r < 1):
    print('\033[31mInvalid option\033[m')
elif r == 1:
    con = bin(n)
    bas = 'Binario'
    print(f'{n} in {bas} is: {con[2:]}')
elif r == 2:
    con = oct(n)
    bas = 'Octal'
    print(f'{n} in {bas} is: {con[2:]}')
elif r == 3:
    con = hex(n)
    bas = 'Hexadecimal'
    print(f'{n} in {bas} is: {con[2:]}')
