R = 0
n1 = float(input('1ª value = '))
n2 = float(input('2ª Value = '))
print('=-' * 13)
while R != 5:
    if R == 4:
        n1 = float(input('1ª value = '))
        n2 = float(input('2ª Value = '))
        print('=-' * 13)
    print(f'''=-  [1] Addition        -= 
=-  [2] Multiplication  -=
=-  [3] Higher value    -=
=-  [4] New values      -=
=-  [5] Exit            -=''')
    print('=-' * 13)
    R = input('Option...= ')
    if R == 1:
        print(f'The sum of the values is {n1 + n2}')
        print('=-' * 18)
    elif R == 2:
        print(f'The multiplication of the values is {n1 * n2:}')
        print('=-' * 18)
    elif R == 3:
        if n1 > n2:
            print(f'the highest value is {n1}')
        if n2 > n1:
            print(f'the highest value is {n2}')
    elif R == 4:
        print('Enter new values...')
    elif R == 5:
        print('Exit...')
        print()
    else:
        print('\033[031mOption invalid\033[m')
