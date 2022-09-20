total = 0
c = 10
Ptr = int(input('1ª termo = '))
Pa = int(input('pa = '))
while c != 0:
    total += c
    while c >= 1:
        c -= 1
        print(Ptr, end=' -> ')
        Ptr += Pa
    print('Stop', end='')
    c = int(input('\n'))
print(total)
