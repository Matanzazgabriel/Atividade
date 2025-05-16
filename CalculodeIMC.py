#Descrição: Solicitar nome, peso e altura. Calcular o IMC através da fórmula:
#IMC = peso / (altura*altura)
#● Mostrar no console o nome e o resultado do IMC (número)
#● Construir uma estrutura de se … senao se com os valores da tabela de IMC.

nome = str (input("Escreva seu nome: "))
peso = float (input("Escreva seu peso: "))
altura = float (input("Escreva sua altura: "))

imc = peso / (altura*altura)

print (f"Seu IMC é: {imc:.2f} ")

if imc <18.5:
    print ("Abaixo do peso")
elif imc >= 18.5 and imc <= 24.9:
    print ("Peso normal")
elif imc >= 25.0 and imc <= 29.9:
    print ("Sobrepeso")
else:
    print ("Obesidade")
    



