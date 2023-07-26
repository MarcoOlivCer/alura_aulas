print("*************************************************************")
print(" Bem Vindo ao jogo de Adivinhação ")
print("*************************************************************")

numero_secreto = 43

chute = input("Digite o seu numero: ")

print(" Voce digitou: ", chute)

chute = int(chute)

if(numero_secreto == chute):
    print("Você acertou!")
else:
    print("Você errou!")    