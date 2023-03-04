n = int(input(''))
f = 1
print(f'{n}!', end=' = ')
print(f'{n} ', end='')
while n > 1:
    n = n - 1
    f = f + (f * n)
    print(f'x {n}', end=' ')
print(f'= {f}', end=' ')
