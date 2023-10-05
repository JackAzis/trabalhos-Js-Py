#um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira
#Ex: Digite um numero: 6.127    o numero 6.127 tem a parte inteira 6
import math
n = float(input('Diga um numero:'))
t = math.trunc (n)
print(f'O numero {n} tem a parte inteira {t}')