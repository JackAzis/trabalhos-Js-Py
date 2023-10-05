#que leia a velocidade de um carro
# se ele ultrapassar 80km/h. mostre uma mensagem dizendo que ele foi multado
#a multa vai custar R$7,00 por cada Km acima do limite
v = int(input('diga a velocidade:'))
if v>80:
    print(f'você foi multado, pague {(v -80)*7}')


