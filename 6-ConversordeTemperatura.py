print ("--------- conversor-----------")

celcius = int (input("Digite a temperatura: "))
fahrenheit = (celcius * 9) + 32
kelvin = celcius + 273.15

print("Escolha uma opção: ")
print("1 - Celsius para Fahrenheit")
print("2 - Celsius para Kelvin")
print("3 - Encerrar")

escolha = 0
while escolha != 3:
    escolha = int(input("Digite a temperatura em Celsius: "))
    if escolha == 1:
        print(f"{celcius}° para Fahrenheit = {fahrenheit}°F")
    if escolha == 2:
        print (f"{celcius}° para Kelvin = {kelvin}°")