numero = 42
total_de_tentativas = 3

while(total_de_tentativas > 0):
    chute =int( input("Digite um numero : "))
    acertou = chute == numero
    maior = chute > numero
    menor = chute < numero

    if acertou :
        print("Você acertou!!! ")
    elif maior:
        print("Você ERROO!!!!, O seu chute foi maior que o numero.")
    elif menor :
        print("Você errou !!!!!!, O seu chute foi menor que o número.")

    total_de_tentativas = total_de_tentativas - 1