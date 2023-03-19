l1 = float(input('l1 = '))
l2 = float(input('l2 = '))
l3 = float(input('l3 = '))
r = 0
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print(f'The measures {l1} {l2} {l3} can form a triangle!')
else:
    print(f'The measures {l1} {l2} {l3} cannot form a triangle!')
if l1 == l2 and l2 == l3:
    print('eq')
elif (l1 == l2 or l2 == l3 or l1 == l3) and (l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2):
    print('is')
elif (l1 != l2 and l2 != l3) and (l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2):
    print('es')
