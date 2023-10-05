#que pergunte a distancia de uma viagem em Km calcule o preço da passagem
#cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas
d = float(input('qual a distancia da viagem: '))

if d <= 200:
    print(f'R${d*0.50:.2f}')
else:
    print(f'R${d*0.45:.2f}')