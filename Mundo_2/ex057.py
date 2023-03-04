genre = ''
while genre != 'M' and genre != 'F':
    genre = input('Genre [M/F]: ').strip().upper()
    if genre != 'M' and genre != 'F':
        print('\033[031m sorry invalid option...\033[m')
if genre == 'M':
    print('genre [M] registration')
if genre == 'F':
    print('genre [F] registration')
'''genre = ' '
while genre != 'M' and genre != 'F':
    genre = input('Genre [M/F]: ').strip().upper()
    if genre not in 'FM':
        print('\033[31m sorry invalid option...\033[m')
print(f'\033[32mGenre [{genre}] registration\033[m')'''
