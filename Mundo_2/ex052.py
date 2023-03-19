C_div = 0
n = int(input(''))
for c in range(1, n + 1):
    if n % c == 0:
        C_div += 1
        print(f'\033[32m{c}\033[m', end=' ')
    else:
        print(f'\033[33m{c}\033[m', end=' ')
print(f'\nThe number {n} has {C_div} divisors')
if C_div == 2:
    print('\033[32:42mThis is a prime number\033[m')
else:
    print('\033[31mNot a prime number!')
