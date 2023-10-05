#faça o computador pensar em um numero inteiro entre 0 e5 e peça para o
#usuario tentar descobrir qual foi o numero escolhido pelo computador
# devera escrever na tela se o usuario venceu ou perdeu
import random
op = [0, 1, 2, 3, 4, 5]
n = int(random.choice(op))
tentativa = int(input('diga qual numero de 0 a 5 eu pensei: '))
if tentativa==n:
    print('acertou mizeravel')
else  :
    print('errrooou')
print(f'o numero era {n}')

