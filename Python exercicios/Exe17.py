#um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo
#calcule e mostre o comprimento da hipotenusa
import math
co = float(input('comprimento do cateto oposto'))
ca = float(input('comprimento do cateto adjacente'))
soma = (co ** 2) + (ca ** 2)
hipo = math.sqrt(soma)
print(f'o comprimento da hipotenusa é {hipo:.2f}')
'''hipo =  math.hypot (co, ca)'''