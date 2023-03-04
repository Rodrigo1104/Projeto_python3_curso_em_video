c = 0
Ptr = int(input('1ª Number = '))
Pa = int(input('pa = '))
while c < 10:
    c += 1
    print(f'{Ptr} -> ' if c < 10 else f'{Ptr} -> Fim', end='')
    Ptr += Pa
