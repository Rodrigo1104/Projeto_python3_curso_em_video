from datetime import date
at = date.today().year
year = int(input('how year were you born? :'))
genre = input('genre ? [1]Male/[2]Female').upper()
year_old = at - year
print('-=-'*10)
print(f'your year of birth was {year}, you have {year_old} in 2022.')
if year_old < 18 and genre == '1':
    f = 18 - year_old
    dal = year + 18
    print(f''' still {f} years to go...
your enlistment is in {dal}''')
elif year_old > 18 and genre == '1':
    p = year_old - 18
    dal = year + 18
    print(f'''you exceeded {p} years of time.
his enlistment was in {dal}''')
elif year_old == 18 and genre == '1':
    print("you need to enlist immediately")
elif genre == '2':
    print("you don't need to enlist")
