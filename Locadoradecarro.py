kmpercorrido = float(input("Quantos km você percorreu: "))
diasalugados = int(input("Dias que você alugou: "))
total = (kmpercorrido*99) + (diasalugados * 0.20)

print ("------------nota fiscal------------")
print (f"[1] - km = R$ {(kmpercorrido * 0.20):.2F}")
print (f"[2] - dias - R$ {(diasalugados *90)}")
print ("=====AAAA LULA, MEU PRESIDENTE==============")
print (f"TOTAL = R$ {total:.2F}")