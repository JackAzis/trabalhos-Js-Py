#um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
#ex: ana maria de souza primeiro:ana  ultimo:souza
nome = str(input('Qual seu nome: ')).strip().split()


print(f'seu primeiro nome é: {nome[0]}\nseu ultimo nome é: {nome[len(nome)-1]} ')
