s = float(input(''))  # salary
i = float(input(''))  # valor house
p = int(input(''))    # years old
if i / (p * 12) <= (s * 30) / 100:
    print('sim')
else:
    print('nao')
