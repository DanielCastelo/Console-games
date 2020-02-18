import random

def abertura():

    print("########################################")
    print("#Ola, bem vindo ao jogo de adivinhação.#")
    print("########################################")

def jogar_adivinhacao():

    abertura()

    numero_secreto =  random.randrange(1,101)
    total_de_tentativas = 0
    rodada = 1
    pontos = 100

    print("Escolha um nível de dificuldade.")
    print("[1] Fácil, [2] Médio ou [3] Difícil.")

    nivel = int(input("Digite o nível: "))

    if(nivel==1):
        total_de_tentativas = 20
    elif(nivel==2):
        total_de_tentativas = 10
    elif(nivel==3):
        total_de_tentativas = 3
    else:
        print("Escolha entre 1, 2 ou 3!")


    for rodada in range(1, total_de_tentativas + 1):


        print("Tentativa {}, restam {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")


        print("Voce digitou " , chute_str)

        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Voce deve digitar um número entre 1 e 100.")
            continue

        acertou = numero_secreto == chute
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if (acertou):
            print("Você Acertou e fez {} pontos!".format(pontos))
            break
        else :
            if(maior):
                 print("Você errou, o seu chute foi muito alto")
            elif (menor):
                print("Você errou, o seu chute foi muito baixo")

        total_de_tentativas = total_de_tentativas - 1
        rodada += 1
        pontos_perdidos = abs(chute - numero_secreto)
        pontos = pontos - pontos_perdidos

    print("Fim do Jogo, pontuação final: {}".format(pontos))

if(__name__ == "__main__"):
    jogar_adivinhacao()