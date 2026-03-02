horas = float(input("Digite suas horas de trabalho: "))
valor_hrs = float(input("Digite o valor das suas horas de trabalho: "))

salario_bruto = horas * valor_hrs
IR = salario_bruto - (11/100)
INSS = salario_bruto - (8/100)
sindicato = salario_bruto - (5/100)
salario_liquido = salario_bruto - INSS - sindicato

print(salario_bruto)
print(IR)
print(INSS)
print(sindicato)
print(f"Seu salário líquido é de {salario_liquido: .2f}")



# TEM QUE ARRUMAR