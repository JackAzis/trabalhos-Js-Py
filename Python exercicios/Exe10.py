# um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos dólares ela pode comprar
# considere US$1.00 = R$3,27
saldo = float(input('Seu saldo é de: R$'))
d = saldo / 3.27
print(f'Com seu saldo de R${saldo} você pode comprar US${d:.2f} ,com a cotação de R$3,27 o dollar')