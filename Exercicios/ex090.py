d_alunos = dict()
d_alunos['Nome'] = str(input('Nome do aluno: '))
d_alunos['Media'] = float(input('Media do Aluno: '))
if d_alunos['Media'] >= 7:
    d_alunos['situacao'] = 'Aprovado'
elif d_alunos['Media'] < 4:
    d_alunos['situacao'] = 'Reprovado'
else:
    d_alunos['situacao'] = 'Recuperação'
print(f'O {d_alunos["Nome"]} teve media: {d_alunos["Media"]} situação: {d_alunos["situacao"]}')
