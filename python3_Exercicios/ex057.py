genre = ''
while genre != 'M' and genre != 'F':
    print('genre? [M/F]')
    genre = input()
    if genre != 'M' and genre != 'F':
        print('\033[031m sorry invalid option...\033[m')
if genre == 'M':
    print('Thank you boy')
if genre == 'F':
    print('Thank you girl')
