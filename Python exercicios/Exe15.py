#Um programa que pergunte a quantidade de Km percorridos por um carro alugado e
#a quantidade de dias pelos quais ele foi alugado, calcule o preço a pagar
#sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado
km = float(input('Quantos Km você percorreu? '))
dias = int(input('Quantos dias você ficou com o carro?'))
diaria = 60 * dias
distancia = 0.15 * km
print(f'Você percorreu {km} e ficou {dias} com o veiculo, \n o que totaliza R${diaria + distancia:.2f}')