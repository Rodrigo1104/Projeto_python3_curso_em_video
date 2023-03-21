RED, RESET = "\033[1;31m", "\033[0;0m"
v = float(input('km/h: '))
if v > 80:
    print(RED + "speeding..." + RESET)
    print(f'you were fined in U$ {((v - 80) * 7) / 5.17:.2f}')
