import random

def abertura():

    print("##################################")
    print("#Ola, bem vindo ao jogo de Forca.#")
    print("##################################")

def jogar_forca():


    abertura()

    arquivo = open("palavras.txt", "r")
    palavras = [] #lista palavras

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)


    arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()

    letra_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    tentativas = 0

    print(letra_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        index = 0

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letra_acertadas[index] = letra
                index += 1
        else:
            tentativas += 1

        enforcou = tentativas == 6
        acertou = "_" not in letra_acertadas
        print(letra_acertadas)

        if(acertou == True):
            print("Parabéns, você venceu!")
        elif(enforcou == True):
            print("Você perdeu, a palavra era: {}".format(palavra_secreta))

    print("Fim de jogo")

if(__name__ == "__main__"):
    jogar_forca()

