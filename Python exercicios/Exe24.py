#um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "santo"
c = str(input('Diga o nome de sua cidade: ')).lower()
c = c.split()
print('santo' in c[0])