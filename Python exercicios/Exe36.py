# para aprovar o  emprestimo canvario para a compra de uma casa o programa vai perguntar
#o valor da casa, o salario do comprador e em quantos anos ele vai pagar
#calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario ou então o emprestimo será negado
valor = float(input('Diga o valor da casa: '))
salario = float(input('Diga quanto você recebe: '))
anos = int(input('Em quantos anos você deseja pagar: ')) *12
trinta = salario * 0.30
prest = valor / anos
if prest > trinta:
    print('Emprestimo negado')
else:
    print(f'{prest:.2f}')