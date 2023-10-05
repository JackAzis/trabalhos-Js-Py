# um programa que leia três numeros e mostre qual é o maior e qual é o menor

a = int(input('Diga o primeiro numero: '))
b = int(input('Diga o segundo numero: '))
c = int(input('Diga o terceiro numero: '))
"""if n1>n2 and n1>n3:
    print(f'{n1} é o maior numero')
if n1<n2 and n1<n3:
    print(f'{n1} é o menor numero')
if n2>n1 and n2>n3:
    print(f'{n2} é o maior numero')
if n2<n1 and n2<n3:
    print(f'{n2} é o menor numero')
if n3>n2 and n3>n1:
    print(f'{n3} é o maior numero')
if n3<n2 and n3<n1:
    print(f'{n3} é o menor numero')"""
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O menor numero é {menor}')
print(f'O maior numero é {maior}')
