numero = 42
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):
    print("Tentativa {} de {}".format(rodada,total_de_tentativas))
    chute =int( input("Digite um numero : "))
    acertou = chute == numero
    maior = chute > numero
    menor = chute < numero

    if acertou :
        print("Você acertou!!! ")
        break
    elif maior:
        print("Você ERROO!!!!, O seu chute foi maior que o numero.")
    elif menor :
        print("Você errou !!!!!!, O seu chute foi menor que o número.")

    rodada = rodada + 1

print("Fim de jogo !!!!!") 