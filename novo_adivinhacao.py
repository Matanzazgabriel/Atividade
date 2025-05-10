import random
numero_secreto = random .randint (1,10)
tentativas = 0
contagem_tentativas = 0
print ("==Bem vindo ao jogo numerico secreto==")
print ("Tente advinhar o numero secreto entre 1 e 10.")
while tentativas != numero_secreto:
    numero = int(input("Digite um numero: "))
    contagem_tentativas = contagem_tentativas+1
    if numero == numero_secreto:
        print("Parabéns, você acertou!!!")
        print(f"Você precisou de {contagem_tentativas}")
        break
    elif numero < numero_secreto:
        print ("O numero secreto é maior. ")
    else:
        print ("O numero secreto é menor.")
    