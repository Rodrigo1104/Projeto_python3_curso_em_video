lista = []
resp = ''
descarte = [1]
while resp in 'SsYy':
    descarte = [str(input('Nome:')), float(input('1ª Nota:')), float(input('2ª Nota:'))]
    lista.append(descarte)
    descarte = []
    resp = input("Gostaria de continuar ")[0]
print('Programa finalizado')

print('=-' * 30)
for c in lista:
    print(f'   {c[0]}\n1ª nota: {c[1]} \n2ª nota: {c[2]}\n media: {(c[1] + c[2])/2}')
    print('==============\n')

r = ''
aluno = ''
while r in 'SsYy':
    r = input('Gostaria de ver o boletim de algum aluno: [S/N]: ')[0]
    aluno = input('Digite o Nome do aluno: ')
    for c in lista:
        if c[0] == aluno:
            print('=-' * 30)
            print(f'{c[0]}\n1ª nota: {c[1]} \n2ª nota: {c[2]}\nmedia: {(c[1] + c[2])/2}\n')
            break
        else:
            print('Aluno não esta Matriculado.')
print('Fim')

