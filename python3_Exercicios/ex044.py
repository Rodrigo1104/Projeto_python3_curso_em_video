v_product = float(input(''))
print('''
[1] MONEI OR CHECK
[2] CREDIT CARD (1X)
[3] CREDIT CARD (2X)
[4] CREDIT CARD (3X +)
''')
payment = int(input(''))
if payment == 1:
    print(f'R$ ={v_product * 0.90:.2f}')
elif payment == 2:
    print(f'R$ ={v_product * 0.95:.2f}')
elif payment == 3:
    print(f'R$ ={v_product * 1.00:.2f}')
elif payment == 4:
    print(f'R$ ={v_product * 1.2:.2f}')
else:
    print('error in payment option')

