p = float(input('Weight? :'))
a = float(input('height? :'))
IMC = p / a ** 2
print(f'IMC is\033[31m {IMC:.2f} \033[m')
if IMC < 18.5:
    print('ab')
elif (IMC == 18.5 or IMC > 18.5) and IMC < 25:
    print('Ideal')
elif (IMC == 25 or IMC > 25) and IMC < 30 or IMC == 30:
    print('sb_peso')
elif (IMC > 30 or IMC > 30) and IMC < 40:
    print('obs')
elif IMC > 40:
    print('ob_morbid')
