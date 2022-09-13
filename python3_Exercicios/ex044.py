vp = float(input('Amount? = '))
print('''
[1] MONEI OR CHECK
[2] CREDIT CARD (1X)
[3] CREDIT CARD (2X)
[4] CREDIT CARD (3X +)
''')
payment = int(input(''))
if payment == 1:
    print(f'R${vp * 0.90:.2f}')
elif payment == 2:
    print(f'1 x {(vp * 0.95) / 1:.2f} = R${vp * 0.95:.2f}')
elif payment == 3:
    print(f'2 x {(vp * 1)/2:.2f} = R${vp * 1:.2f}')
elif payment == 4:
    np = int(input('x '))
    print(f'{np} x {(vp * 1.2) / np:.2f} = R${vp * 1.2:.2f}')
else:
    print('error in payment option')
