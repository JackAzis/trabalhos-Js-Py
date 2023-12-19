import random

def nome_jogo():
    print("#################################")
    print("###### BEM VINDO AO JOGO ########")
    print("############ FORCA ##############")
    print("#################################")

def vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print(f"Que pena você perdeu, a palavra era {palavra_secreta}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |         X         |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def jogar():
    
    nome_jogo()

    arquivo = open("frutas.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    numero = random.randrange(0, len(palavras))
    
    palavra_secreta = palavras[numero].upper()
    letras_certas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0
    
    dificuldade = int(input("Escolha a dificuldade, 1 fácil, 2 médio, 3 forca: "))
    
    if (dificuldade == 1):
        chances = 20
    elif(dificuldade == 2):
        chances = 14
    else:
        chances = 7
    
    print(f"Dificuldade {dificuldade} selecionada, você tem {chances} chances  ")
    #enquanto true continua executando
    while(not enforcou and not acertou):
        
        chute = input("Diga uma letra: ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_certas[index] = letra

                index = index + 1
        else:
            erros = erros + 1
            print(f"A letra {chute} não esta na palavra, você ainda tem {chances - erros} chances")
        enforcou = erros == chances
        desenha_forca(erros)
        acertou = "_" not in  letras_certas
        print(letras_certas)
    if(acertou):
        vencedor()
    else:
        perdedor(palavra_secreta)
    
if (__name__ == "__main__"):
    jogar()