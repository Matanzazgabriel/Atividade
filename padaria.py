frances = integral = docefarofa = doceliso = forma = numero = 0
valorfrances = valorintegral = valordocefarofa = valordoceliso = valorforma = 0

while numero !=6:
    print ("-------Padaria-------")
    print ("[1]Pão frances")
    print ("[2]Pão integral")
    print ("[3]Pão doce farofa")
    print ("[4]Pão doce liso")
    print ("[5]Pão de forma")
    print ("[6]Saindo do cardápio")
    opcao = int (input("Escolha sua opção: "))
    
    if opcao ==1:
        frances = int(input("Digite a quantidade de pão francês que você quer :"))
        valorfrances = frances * 1.04
    elif opcao ==2:
        integral = int(input("Digite a quantidade de pão integral que você quer:"))
        valorintegral = integral * 1.04
    elif opcao ==3:
        docefarofa = int(input("Digite a quantidade de pão doce farofa que você quer:"))
        valordocefarofa = docefarofa *1.11
    elif opcao ==4:
        doceliso = int(input("Digite a quantidade de pão doce liso que você quer:"))
        valordoceliso = doceliso * 1.08
    elif opcao ==5:
        forma = int(input("Digite a quantidade de pão de forma que você quer:"))
        valorforma = forma *0.95
    elif opcao ==6:
        
        break
    
    print ("---------Recibo----------")
    
    if frances > 0:
        print (f"Pão francês : {frances} unidade(s) - R$ {valorfrances:.2f}")
    if integral > 0:
        print (f"Pão integral: {integral} unidade(s) - R$ {valorintegral:.2f}")
    if docefarofa > 0:
        print (f"Pão doce farofa {docefarofa} unidade(s) - R$ {valordocefarofa:.2f}")
    if doceliso > 0:
        print ((f"Pão doce liso {doceliso} unidade(s) - R$ {valordoceliso:.2f}"))
    if forma > 0:
        print ((f"Pão de forma {forma} unidade(s) - R$ {valorforma:.2f}"))
    total = valorfrances + valorintegral + valordoceliso + valorforma  
    print (f"Valor total a pagar: {total:.2f}")                        
        