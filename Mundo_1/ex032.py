from datetime import date
a = int(input('year? :'))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(f'the year {a} is leap year')
else:
    print(f'the year {a} is not a leap year')
