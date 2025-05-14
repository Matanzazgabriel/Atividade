#Entrada de dados
#Cálculo das prestações
#Exibição dos resultados
valordacompra =int(input("valor da compra: ")) 
valordeparcelas =int(input("Quantas vezes você quer parcelar ?"))
prestacao =valordacompra /valordeparcelas

print (f"valor da compra é: {valordacompra}")
print (f"valor das {valordeparcelas} prestacoes é: {prestacao:.2f}")
