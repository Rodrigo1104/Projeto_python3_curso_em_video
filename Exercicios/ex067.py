while True:
        n = int(input(f'Que ver a tabuada de qual valor? : '))
        if n < 0:
            break
        print('=-' * 20)
        for c in range(1, 11):
            print(f'{n} x {c} = {n*c}')
        print('=-' * 20)
print('FIM DO PROGRAMA')
