c = total_gasto = mais_de_1000 = menor_preco = 0
while True:
    c += 1
    if c == 1:
        print('==== MERCADINHO LEVE MENOS E PAGUE MAIS ====')
    nome_produto = str(input('Nome do produto? '))
    preco_produto = float(input(f'Preço {nome_produto}: R$'))
    total_gasto += preco_produto
    print('Produto adicionado')
    print('-='*15)
    if c == 1:
        produto_mais_barato = nome_produto
        menor_preco = preco_produto
    elif preco_produto < menor_preco:
        produto_mais_barato = nome_produto
        menor_preco = preco_produto
    if preco_produto > 1000:
        mais_de_1000 += 1
    op = ' '
    while op not in 'SN':
        try:
            op = input('Que continuar? [S/N] ? ').strip().upper()[0]
            print('-=' * 15)
        except:
            continue
    if op == 'N':
        break
if mais_de_1000 > 0:
    print(f'{mais_de_1000} produtos que custaraam mais de 1.000,00')
print(f'total da compra R${total_gasto}\n{produto_mais_barato} foi o produto mais barato')


