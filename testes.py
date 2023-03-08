RED, BLUE, CYAN, GREEN, RESET = "\033[1;31m", "\033[1;34m", "\033[1;36m", "\033[0;32m", "\033[0;0m"
s = float(input(''))
cor = ''
if s < 1000:
    cor = RED
else:
    cor = BLUE
print(f'R${cor}{s:_.2f}{RESET}'.replace('.', ',').replace('_', '.'))
