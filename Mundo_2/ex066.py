c = s = 0
while True:
    n = int(input(f'Enter a value or [999 to STOP] : '))
    if n == 999:
        break
    c += 1
    s += n
print(f'A soma dos {c} valores é: {s}')