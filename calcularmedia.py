#programa { funcao inicio()
          #{ //algoritmo "media_notas" //var real nota1, nota2, media 
          # escreva("Digite a primeira nota: ") 
          # leia(nota1) 
           #escreva("Digite a segunda nota: ") 
           #leia(nota2) media = (nota1 + nota2) / 2 
           #escreva("\nMédia: ", media) 
           
           #se (media>=7){ escreva("\nAprovado!") } 
           #senao { escreva ("\n Reprovado!") } } }

#nota1 = float
#nota2 = float 
#media = float

nota1 = float(input("Digite a primeira nota: "))
print(f"O resultado é: {nota1}")
nota2 = float(input("Digite a segunda nota: "))
print(f"O resultado é: {nota2}")

media= (nota1+nota2)/2
print(f"A media é: {media:2f}")

if media>=7:
    print ("Aprovado ")
else :
    print("Reprovado ")

