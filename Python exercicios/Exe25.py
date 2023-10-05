#um programa que leia o nome de uma pessoa e diga se ela tem 'silva' no nome
nome = str(input('Seu nome completo: ')).lower()
print(f"seu nome é {nome} você é um silva: {'silva' in nome}")