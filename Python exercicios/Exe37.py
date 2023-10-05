#leia um numero inteiro e peça ao usuario escolher qual sera a base de conversão
#1 binario 2 octal 3 hexadecimal
n = int(input('Diga o numero: '))
conv = str(input('Digite o numero indicado para a conversão desejada\n'
                 '1 para binario, 2 para octal e 3 para hexadecimal: '))
binary = bin(n)
octal = oct(n)
hexa= hex(n)
if conv == '1':
    print(f"{n} convertido em binario é {format(n, 'b')}")
elif conv == '2':
    print(f"{n} convertido em octal é {format(n, 'o')}")
elif conv == '3':
    print(f"{n} convertido em hexadecimal é {format(n, 'x')}")

