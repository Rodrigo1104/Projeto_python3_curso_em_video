n = int(input('Que ver a tabuada de qual número?: '))
print('==='*4)
c = 0
while c < 10:
    c += 1
    print(f'{n} + {c} = {n + c}')
    if c == 10:
        print('==='*4)
c = 0
while c < 10:
    c += 1
    print(f'{n} - {c} = {n - c}')
    if c == 10:
        print('==='*4)
c = 0
while c < 10:
    c += 1
    print(f'{n} x {c} = {n * c}')
    if c == 10:
        print('==='*4)
c = 0
while c < 10:
    c += 1
    print(f'{n} / {c} = {n / c:.1f}')
    if c == 10:
        print('==='*4)
c = 0
