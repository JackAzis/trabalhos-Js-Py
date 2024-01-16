'''numeros = [1,2,3,4,5,6,7,8,9,10] 
nomes = ['paulo', 'david', 'silva', 'gama']
anos = [1995, 2024]'''
""""
for numero in numeros:
    print(numero)
for nome in nomes:
    print(nome)
"""

'''for numero in numeros:
    if numero % 2 == 1:
        sum(numero)
        print(f'{numero}')'''

'''for numero in numeros: 
    print(numeros.reverse)'''

'''numero_tabuada = int(input("Digite um número para a tabuada: "))
for i in range(1, 11):
    resultado = numero_tabuada * i
    print(f"{numero_tabuada} x {i} = {resultado}")'''


lista_numeros = [10, 5, 8, 3, 7]
soma = 0

try:
    for numero in lista_numeros:
        soma += numero
    print(f"Soma dos elementos: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
