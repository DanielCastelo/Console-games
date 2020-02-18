import forca
import adivinhacao

print("########################")
print("#Ola, escolha seu jogo.#")
print("########################")

print("[1] Adivinhação, [2] Forca")

jogo = int(input("Qual jogo?"))

if(jogo==1):
    print("Jogando Adivinhação")
    adivinhacao.jogar_adivinhacao()
elif(jogo==2):
    print("Jogando Forca")
    forca.jogar_forca()