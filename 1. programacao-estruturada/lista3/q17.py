inicio = int(input("valor inicial: "))
fim = int(input("valor final: "))
if inicio > fim:
    print(f"o numero inicial nao pode ser maior que o final")
else:
    cont_par = 0
    cont_impar = 0
    soma_par = 0
    soma_impar = 0
    for i in range (inicio, fim+1):
            if i % 2 == 0:
                cont_par += i
                soma_par += 1
                print(f"{soma_par}, {cont_par}")
            else:
                cont_impar += i
                soma_impar += 1
                print(f"{soma_impar}, {cont_impar}")
    media_impar = soma_impar / cont_impar
