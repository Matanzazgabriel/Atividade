opcao = - 1
while opcao != 0:
    print("--- Calculadora ---") 
    print("1 - Somar") 
    print("2 - Subtrair") 
    print("3 - Multiplicar") 
    print("4 - Dividir") 
    print("0 - Sair")

    opcao =int (input ("Escolha uma opção: "))

    if opcao == 0:
        print("Calculadora encerrada!")
        break
        
    if opcao in [1, 2, 3, 4]:
        num1 = int (input("Digite o primeiro numero: "))
        num2 = int (input("Digite o segundo numero: "))
        
    if opcao == 1:
        resultado = num1 + num2
        print(f"O resultado da soma é {resultado}")
        
    if  opcao == 2:
        resultado = num1 - num2
        print(f"O resultado da subtração é {resultado}")
        
    if  opcao == 3:
        resultado = num1 * num2
        print(f"O resultado da multiplicação é {resultado}")
        
    if opcao == 4:
        resultado = num1 / num2
        print(f"O resultado da divisão é {resultado}")
    
    #olhar com a professora
    

    

    
    
    
    
