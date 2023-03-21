c = 1
s = 0
n = 0
up = n
down = n
while True:
    n = float(input(f'{c}ª Number = '))
    if n == 0:
        break
    print(f'[{n}] Registered... ')
    print('=-'*15)
    c += 1
    s += n
    if (n < down) or (down == 0):
        down = n
    if n > up:
        up = n
print(f'Registered {c - 1} numbers\nthe smallest value is {down}\nthe greatest value is {up}\nthe average is = {s / (c - 1)}')
