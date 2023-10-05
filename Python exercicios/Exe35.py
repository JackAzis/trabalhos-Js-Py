#leia o comprimento de três retas e diga ao usuario se elas podem ou não formar um triangulo
r1 = float(input('Diga a primeira reta: '))
r2 = float(input('Diga a segunda reta: '))
r3 = float(input('Diga a terceira reta: '))
if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print(f'é possivel formar um triangulo')
else:
    print(f'não é possivel formar um triangulo')