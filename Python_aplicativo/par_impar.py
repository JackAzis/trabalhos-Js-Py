n = int(input('Digite um numero e eu direi se é par ou impar '))
n_str = str(n)
ultimo_digito = int(n_str[-1])

if ultimo_digito in (0, 2, 4, 6, 8):
    print(f'O numero {n} é Par')
elif ultimo_digito in (1, 3, 5, 7, 9):
    print(f'O numero {n} é Impar')
else:
    print('Por favor digite um numero inteiro válido')

#numero = int(input("Digite um número: "))
#if numero % 2 == 0:
#    print("O número é par.")
#else:
#    print("O número é ímpar.")
