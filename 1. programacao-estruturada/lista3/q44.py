while True:
    try:
        valores = input("digite os valores: ").split()

        if len (valores)!=10:
            print("digite apenas  10 valores")
            continue

        numeros = [float(x) for x in valores]
        break
    except ValueError:
        print(f"digite apenas numeros")

dentro = 0
fora = 0

for n in numeros:
    if 10<= n >= 30:
        dentro += 1
    else:
        fora += 1

print(f"total de números dentro do intervalo: {dentro}")
print(f"total de números fora do intervalo: {fora}")































'''
try:
    dentro = 0
    fora = 0

    for i in range(10):
        #raise TypeError("digite apenas um número por vez")
        valores =  float(input("Digite o valor: "))

        if 10 <= valores <= 30:
            dentro +=1
        else:
            fora += 1

    print(f"Total de números dentro do intervalo: {dentro}")
    print(f"Total de números fora do intervalo: {fora}")

except:
    print("Digite um número de cada vez")
except ValueError:
    print("Você deve digitar apenas números")
'''