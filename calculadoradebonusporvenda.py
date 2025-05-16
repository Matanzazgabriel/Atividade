#calculo da comissão
#Calculo do salario final
#Verificação da meta 

#O usuário insere o nome do vendedor, o salário fixo e o total de vendas efetuadas.
nomeVendedor= str (input("Informe o nome do vendedor: ")) 
salarioFixo= int (input("Informe o salario fixo: ")) 
totalVendas= int (input("Informe o total de vendas: ")) 

#A comissão (bonus) é calculada como 15% (0,15) do salário fixo.

bonus = salarioFixo * 0.15
salarioRecebido = salarioFixo + bonus
print (f"O salario final é: {salarioRecebido}")

#Se o vendedor tiver feito 20 ou mais vendas, é exibida uma mensagem indicando que a meta foi atingida, 
# junto com o valor do salário final e o valor da comissão.
#○ Caso contrário, apenas uma mensagem de que a meta não foi atingida é exibida.

if totalVendas>=20:
    print("Meta foi atingida")
else:
    print ("Meta não foi atingida")
    