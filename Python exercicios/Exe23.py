#um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
#digite um numero:1834 unidade:4 dezena:3 centena:8 milhar:1
n = int(input('Digite um numero:'))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n// 1000 % 10
print(f'unidade:{u}\ndezena:{d}\ncentena:{c}\nmilhar:{m}')
