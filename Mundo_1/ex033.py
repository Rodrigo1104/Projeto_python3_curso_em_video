RED, BLUE, CYAN, GREEN, RESET = "\033[1;31m", "\033[1;34m", "\033[1;36m", "\033[0;32m", "\033[0;0m"
n = int(input('1ª number: '))
la = n
sm = n
n = int(input('2ª number: '))
if n > la:
    la = n
if n < sm:
    sm = n
n = int(input('3ª number: '))
if n > la:
    la = n
if n < sm:
    sm = n
print(f'the highest value was {RED}{la}{RESET}, and the lowest value was {RED}{sm}{RESET}')
