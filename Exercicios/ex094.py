from time import time
dados = []
mulheres = []
maior = []
media = 0
while True:
    pessoas = {}    
    pessoas['nome'] = str(input('Nome: '))
    pessoas['sexo'] = str(input('M/F: '))
    pessoas['idade'] = int(input('Idade'))
    r = input('0 - 1')
    if pessoas['sexo'] in str(pessoas['sexo']): 
        mulheres.append(pessoas)
    dados.append(pessoas)
    media += (int((pessoas['idade'])))
    if r == '0':
        break
print(dados)
print(len(dados))
print(mulheres)
print(media / len(dados))