import random
def jogar():

    print("#################################")
    print("###### BEM VINDO AO JOGO ########")
    print("########## ADIVINHAÇÃO ##########")
    print("#################################")

    resposta = random.randrange(1,101)
    pontos = 1000
    total_de_tentativas = 0

    print(f'Escolha o nivel de dificuldade 1 para facil, 2 para médio e 3 para dificil')
    nivel = int(input(f'Nivel: '))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print(f'Tentativa {rodada} de {total_de_tentativas}')
        
        chute = input('Digite um numero entre 1 e 100: ')
        print("Você digitou: ", chute)
        chute = int(chute)

        acertou = chute == resposta
        maior = chute > resposta
        menor = chute < resposta

        if(chute < 1 or chute > 100):
            print("O numero deve ser entre 1 e 100: ")
            continue
        if(acertou):
            print(f'Parabens o numero era {resposta} e você fez {pontos}')
            break
        else :
            if(maior):
                print("O numero é menor do que", chute)
            elif(menor):
                print("O numero é maior do que", chute)
            erros = abs(resposta - chute)
            pontos = pontos - erros
        rodada = rodada + 1
    print("#Game Over#")

if (__name__ == "__main__"):
    jogar()