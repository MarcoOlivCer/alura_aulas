import random

print("*************************************************************")
print(" Bem Vindo ao jogo de Adivinhação ")
print("*************************************************************")

#numero que o usuario tem que acertar e total de tentativas do usuario
#função randrange serve par gerar numeros aleatorios de 1 até 100
numero_secreto = round(random.randrange(1, 101))
total_de_tentativas = 0

print("Qual o nível de dificuldade ?")
print("(1) Fácil (2) Médio (3)Difícil")

nivel = int(input("Define o nível: "))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

#utilizando while
while(rodada <= 3):
    
    print("Tentativa {} de {}". format(rodada, total_de_tentativas))
    #recebendo o input/entrada do usuario
    chute_str = input("Digite o seu numero: ")
    print("Voce digitou: ", chute_str)

    #converter o input/entrada do usuario de string para inteiro
    chute = int(chute_str)
    
    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    #variaveis que são usandas na condição para saber se o usuario acertou ou errou
    acertou = numero_secreto == chute
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    #condição logica para saber se o usuario acertou ou errou
    if(acertou):
        print("Você acertou!")
        break
    else:
        if(maior):
            print("Você errou!, O seu chute foi maior que o número secreto.")
        elif(menor):
            print("Você errou!, O seu numero foi menor que o numero secreto.")      
    
    rodada = rodada + 1

    
print("Fim do jogo!")  