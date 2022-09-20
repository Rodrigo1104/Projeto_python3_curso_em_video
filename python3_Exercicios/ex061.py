c = 1
Ptr = int(input('1ª termo = '))
Pa = int(input('pa = '))
print(Ptr, end=' -> ')
while c < 9:
    c += 1
    Ptr += Pa
    print(Ptr, end=' -> ')
print(f'{Ptr + Pa}', end='')
