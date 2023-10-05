#que pergunte o salario de um funcionario e calcule o valor do seu aumento
#para salarios superiores a R$1250,00 calcule um aumento de 10%
#para os inferiores ou iguais o aumento é de 15%

sal = float(input('quanto é o seu salario: '))
dez = sal * 0.1
quin = sal * 0.15
if sal>1250.00:
    print(f'seu aumento é de R${dez} agora você recebe R${sal+dez}')
if sal<=1250.00:
    print(f'seu aumento é de R${quin} agora você recebe R${sal+quin}')