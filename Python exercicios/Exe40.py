#Leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final
#de acordo com a média atingida
#média abaixo de 5.0   reprovado
#media entre 5.0 e 6.9 recuperação
#média 7.0 ou superior aprovado
t = float(input('Qual foi a nota do teste: '))
p = float(input('Qual foi a nota da prova: '))
m = (t+p)/2
print(f'Sua média foi de: {m}')
if m<5:
    print(f'\033[31mReprovado\033[m')
elif m==5 or m<= 6.9:
    print(f'\033[33mRecuperação\033[m')
elif m>=7:
    print(f'\033[34mAprovado\033[m')