#leia dois numeros inteiros e compare-os mostrandona tela a uma mensagem:
# o primeiro valor é maior, o segundo valor é maior,
# não existe valor maior os dois são iguais
n1 = int(input('Diga o primeiro numero: '))
n2 = int(input('Diga o segundo numero: '))
if n1>n2:
    print(f'{n1} é maior que {n2}')
elif n2>n1:
    print(f'{n2} é maior que {n1}')
else:
    print(f'os numeros são iguais')