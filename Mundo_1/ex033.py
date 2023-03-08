RED, BLUE, CYAN, GREEN, RESET = "\033[1;31m", "\033[1;34m", "\033[1;36m", "\033[0;32m", "\033[0;0m"
n = int(input('1ª Número: '))
la = n
sm = n
n = int(input('2ª Número: '))
if n > la:
    la = n
if n < sm:
    sm = n
n = int(input('3ª Número: '))
if n > la:
    la = n
if n < sm:
    sm = n
print(f'O maior numero digitado foi {RED}{la}{RESET}, e o menor numero foi {RED}{sm}{RESET}')
