#um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
p = float(input('Qual o valor da banana? R$'))
d = p * 0.05
print(f'Promoção! Banana de R${p} por R${p - d:.2f} com 5% de desconto')