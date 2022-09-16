n = int(input('Number? :'))
c = 0
for c in range(1, 11):
    print(f'{n} + {c} = {c + n}')
    if c == 10:
        print('+-*/'*3)
c = 0
while c < 10:
    c += 1
    print(f'{n} - {c} = {c - n}')
    if c == 10:
        print('+-*/'*3)
c = 0
while c < 10:
    c += 1
    print(f'{n} x {c} = {c * n}')
    if c == 10:
        print('+-*/'*3)
c = 0
while c < 10:
    c += 1
    print(f'{n} / {c} = {c / n:.1f}')
    if c == 10:
        print('+-*/'*3)
c = 0
