altura = float(input("Digite sua altura: "))
sexo = str(input("Digite seu sexo: "))
if sexo == "M" or sexo == "m":
    peso = (72.7*altura) - 58
    print(peso)
elif sexo == "F" or sexo == "f":
    peso = (62.1*altura) - 58
    print(peso)
