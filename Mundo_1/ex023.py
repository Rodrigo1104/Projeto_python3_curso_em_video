n = int(input(''))
print('{}U, {}D, {}C, {}M'.format((n % 10), (n // 10 % 10), (n // 100 % 10), (n // 1000 % 10)))
