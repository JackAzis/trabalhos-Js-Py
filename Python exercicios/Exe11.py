#um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta, pinta uma area de  2m²
a = float(input('Qual a altura da parede? '))
l = float(input('Qual a largura da parede? '))
area = a * l
li = area / 2
print(f'sua parede de {a}m de altura e {l}m de largura tem,{area}m²,\n sendo necessario {li}L de tinta para pintala ')