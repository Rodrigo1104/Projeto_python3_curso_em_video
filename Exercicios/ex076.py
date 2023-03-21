tabela_produto = ('lapiz', 1, 'CANETA', 1.5, 'CADERNO', 25,
                  'MOCHILA', 150, 'ESTOJO', 28.00, 'COMPAÇO', 35,
                  'REGUA', 3, 'BORRACHA', 0.50, 'TABOADA', 2,
                  'CADERNO DESENHO', 23.5, 'CAUCULADORA', 13, 'ESCALIMETRO', 16)
print('=' * 40)
print(f'{"LISTA DE PREÇO":-^40}')
print('=' * 40)
for pos, p in enumerate(tabela_produto):
    if pos % 2 == 0:
        print(f'{p:_<30}', end=' ')
    else:
        print(f'R$ {p:>6.2f}')
print('=' * 40)
