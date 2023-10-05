#sortear a ordem de apresentação de trabalho dos alunos
#leia o nome dos quatro alunos e mostre a ordem sorteada
import random
n1 = str(input('nome do primeiro aluno: '))
n2 = str(input('nome do segundo aluno: '))
n3 = str(input('nome do terceiro aluno: '))
n4 = str(input('nome do quarto aluno: '))
alunos = [n1, n2, n3, n4]
random.shuffle(alunos)
print(f' a ordem da apresentação sera {alunos}')