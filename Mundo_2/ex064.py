c = 0
s = 0
n = 0
while n != float(999):
    n = float(input('Exit-[999] or Enter Number: '))
    if n != float(999):
        c += 1
        s += n
print(f'{c} Number = {s}')
