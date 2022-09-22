c = t1 = t2 = t3 = 1
n = int(input('Number: '))
if n < 4:
    for n in range(0, n):
        n += 1
while c < n - 2:
    c += 1
    t1 = t2
    t2 = t3
    t3 = t1 + t2
    print(f'0 -> {t1} -> {t2} -> {t3}' if c == 2 else f'-> {t3}', end=' ')
print('Fim' if n == 0 else '-> Fim', end='')