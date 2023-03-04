l1 = float(input(''))
l2 = float(input(''))
l3 = float(input(''))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print(f'The measures {l1} {l2} {l3} can form a triangle!')
else:
    print(f'The measures {l1} {l2} {l3} cannot form a triangle!')
