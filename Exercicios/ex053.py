for c in range(0, 7):
    Frase = input('').strip().upper().replace(' ', '')
    if (Frase[::-1]) == Frase:
        print('yes')
    else:
        print('No')
