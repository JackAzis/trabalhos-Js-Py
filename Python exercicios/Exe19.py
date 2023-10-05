#Um professor quer sortear um dos seus quatro alunos para apagar o quadro, faça um programa que ajude
#lendo o nome deles e escrevendo o nome do escolhido
import random
a = str(input('diga o nome do primeiro aluno: '))
b = str(input('diga o nome do segundo aluno: '))
c = str(input('diga o nome do terceiro aluno: '))
d = str(input('diga o nome do quarto aluno: '))
'''nomes = a,b, c, d
def selectRandom(nomes):
 return random.choice(nomes)'''
nomes = [a, b, c, d]
print(f'dentre os alunos {a, b, c, d} o sorteado a limpar o quadro é o {random.choice(nomes)}')