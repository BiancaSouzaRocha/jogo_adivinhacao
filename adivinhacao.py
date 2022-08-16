import random


print("#################################")
print("Bem vindo ao Jogo de Adivinhação!")
print("#################################")
numero_secreto = random.randrange(1, 50)
total_tentativas = 3

for rodada in range (1, total_tentativas + 1):
    print(f"Tentativa {rodada} de {total_tentativas}")
    chute_str = input("Digite um número entre 1 e 50: ")
    chute = int(chute_str)

    if (chute < 1 or chute > 50):
        print("Você deve digitar um número entre 1 e 50.")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior do que o número secreto")
        elif (menor):
            print("Você errou! O seu chute foi menor do que o número secreto")

print("Fim de Jogo!")