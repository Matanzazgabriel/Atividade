ano_atual =2025
ano_nascimento = int(input("Digite seu ano de nascimento: "))
idade = ano_atual - ano_nascimento
print (f"Voce tem {idade} anos.")
if idade <16:
    print ("Voce não pode votar! ")
elif idade <18 or idade >70:
    print ("Seu voto é facultativo!")
    