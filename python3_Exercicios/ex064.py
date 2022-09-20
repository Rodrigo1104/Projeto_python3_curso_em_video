c = 0
s = 0
n = 0
while n != float(999):
    n = float(input(''))
    if n != float(999):
        c += 1
        s += n
        print(f'{c}ª number is {n}')
    print('Enter [999] to sum and EXIT')
