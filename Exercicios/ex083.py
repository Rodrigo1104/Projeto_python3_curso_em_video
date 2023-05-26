lista_parenteses = []
exprecao = str(input('Digite sua expreção: '))
for p in exprecao:
    if '(' in p:
        lista_parenteses.append(p)
    if ')' in p:
        lista_parenteses.append(p)
ver = []
for parentese in lista_parenteses:
    if parentese == '(':
        ver.append('(')
    elif parentese == ')':
        if len(ver) > 0:
            ver.pop()
        else:
            ver.append(')')
            break
print(ver)
if len(ver) > 0:
    print('essa expreção é invalida')
else:
    print('valida')
print("test desktop")