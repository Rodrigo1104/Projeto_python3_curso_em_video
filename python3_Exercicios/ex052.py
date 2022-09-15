C_div = 0
n = int(input(''))
for c in range(2, n):
    if n % c == 0:
        C_div += 1
    if C_div > 2:
        print('N')
    else:
        print('S')


