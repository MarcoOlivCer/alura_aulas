print("*************************************************************")
print(" Bem Vindo ao jogo de Adivinhação ")
print("*************************************************************")

#numero que o usuario tem que acertar
numero_secreto = 43
#recebendo o input/entrada do usuario
chute_str = input("Digite o seu numero: ")
print("Voce digitou: ", chute_str)

#converter o input/entrada do usuario de string para inteiro
chute = int(chute_str)

#variaveis que são usandas na condição para saber se o usuario acertou ou errou
acertou = numero_secreto == chute
maior   = chute > numero_secreto
menor   = chute < numero_secreto

#condição logica para saber se o usuario acertou ou errou
if(acertou):
    print("Você acertou!")
else:
    if(maior):
        print("Você errou!, O seu chute foi maior que o número secreto.")
    elif(menor):
        print("Você errou!, O seu numero foi menor que o numero secreto.")      
    

    
print("Fim do jogo!")  