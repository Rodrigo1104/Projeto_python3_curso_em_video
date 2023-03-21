l1 = float(input(''))
l2 = float(input(''))
l3 = float(input(''))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print(f'As medidas {l1} {l2} {l3} Podem formar um triângulo!')
else:
    print(f'As medidas {l1} {l2} {l3} não podem formar um triângulo!')
