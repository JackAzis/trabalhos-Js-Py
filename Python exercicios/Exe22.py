#um programa completo de uma pessoa e mostre
#o nome com todas as letras maiusculas  o nome com todas minusculas
#quantas letras ao todo (sem considerar espaços)
#quantas letras tem o primeiro nome
nome = str(input('Diga seu nome: ')).strip()
print(f'maiusculo: {nome.upper()}')
print(f'minusculo: {nome.lower()}')

print(f"letras: {len(nome) - nome.count(' ')}")
nome = nome.split()

print(f'quantas letras tem o primeiro nome: {len(nome[0])}')
