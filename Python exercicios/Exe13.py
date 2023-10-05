#um programa que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
s = float(input('Quanto você ganha? R$'))
a = s * 0.15
n = s + a
print(f'seu salario era de R${s}, você teve um aumento de R${a} de 15%, agora seu salario é de R${n}')