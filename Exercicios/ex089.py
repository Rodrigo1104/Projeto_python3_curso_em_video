lista = [
    ["Ana", 8.5, 7.0],
    ["Carlos", 6.0, 9.5],
    ["Bianca", 7.5, 8.0],
    ["Daniel", 9.0, 6.5],
    ["Eduarda", 5.0, 8.5],
    ["Felipe", 7.0, 7.5],
    ["Gabriela", 8.0, 9.0],
    ["Henrique", 6.5, 6.0],
    ["Isabela", 9.5, 7.5],
    ["João", 8.0, 6.0]
]
# resp = ''
# descarte = [1]
# while resp in 'SsYy':
#     descarte = [str(input('Nome:')), float(input('1ª Nota:')), float(input('2ª Nota:'))]
#     lista.append(descarte)
#     descarte = []
#     resp = input("Gostaria de continuar ")[0]
# print('Programa finalizado')

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
        print('Aluno não esta Matriculado.')
print('Fim')

