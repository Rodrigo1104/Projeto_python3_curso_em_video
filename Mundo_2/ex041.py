from datetime import date
yb = int(input(''))
age = date.today().year - yb
print(age)
if age <= 9:
    print('Little')
elif (age > 9) and (age <= 14):
    print('Childish')
elif (age > 14) and (age <= 19):
    print('Junior')
elif (age > 19) and (age <= 20):
    print('Senior')
else:
    print('\033[031mMaster\033[m')
