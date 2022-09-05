from datetime import date
yb = int(input(''))
age = date.today().year - yb
if age < 9 or age == 9:
    print('0')
elif age > 9 and age == 14 or age < 14:
    print('1')
elif age > 14 and age == 19 or age < 19:
    print('2')
elif age > 19 and age == 20 or age < 20:
    print('3')
else:
    print('4')
