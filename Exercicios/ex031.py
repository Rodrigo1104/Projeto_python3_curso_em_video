km = int(input('km: '))
if km <= 200:
    print(f'{km}km = U${(km * 0.5)/5.17:.2f}')
else:
    print(f'{km}km = U${(km * 0.45)/5.17:.2f}')


