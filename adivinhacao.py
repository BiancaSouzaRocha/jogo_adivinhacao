print("#################################")
print("Bem vindo ao Jogo de Adivinhação!")
print("#################################")

chute_str = input("Digite um número: ")
chute = int(chute_str)

print(f"Você digitou {chute}")

numero_secreto = 42
acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if (chute):
    print("Você acertou!")
else:
    if (maior):
        print("Você errou! O seu chute foi maior do que o número secreto")
    elif (menor):
        print("Você errou! O seu chute foi maior do que o número secreto")
print ("Fim do jogo!")