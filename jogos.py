import forca, adivinhacao
def escolha_jogo()
    print("#################################")
    print("##### BEM VINDO AO SELETOR ######")
    print("########### DE JOGOS ############")
    print("#################################")

    print("Escolha o jogo")
    print("[1] Forca [2] Adivinhação")

    jogo = int(input("Qual jogo?"))

    if (jogo == 1):
        print("Jogando Forca")
        forca.jogar()
    elif (jogo == 2):
        print("Jogando Adivinhação")
        adivinhacao.jogar()





if (__name__ == "__main__"):
    jogar()