conjunto_de_palavras = ('Caneca', 'tela', 'Camisa', 'pijama', 'boleto', 'controle', 'boneco',)
for palavras in conjunto_de_palavras:
    print(f'\nNa palavra {palavras.upper()} temos as vogais: ', end='')
    for letra in palavras:
        if letra in 'aeiou':
            print(f'{letra}', end='')

