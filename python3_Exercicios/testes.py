Frase = input('').strip().upper().replace(' ', '')
for letters in range(len(Frase) - 1, -1, -1):
    print(Frase[letters], end='')
if Frase == Frase[::-1]:
    print(f' = {Frase[::-1]}\n \033[32mIs Polindromo')
else:
    print(f' = {Frase[::-1]}\n \033[31mNot is Polindromo')
