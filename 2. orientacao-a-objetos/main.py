from funcionario import Funcionario
from datetime import date


funcionarios = []
funcionarios.append(Funcionario("Jessica", date(2004, 4, 28), "Dev-Jr", "TI",
                                date(2024, 12, 6), 10, 15))
funcionarios.append(Funcionario("Gabriel", date(2004, 4, 28), "Dev-Senior", "TI",
                                date(2024, 12, 6), 10, 15))
funcionarios.append(Funcionario("Murilo", date(2004, 4, 28), "Dev-Jr", "TI",
                                date(2024, 12, 6), 10, 15))
funcionarios.append(Funcionario("Fulano", date(2004, 4, 28), "Supervisor", "RH",
                                date(2024, 12, 6), 10, 15))


print("--FUNCIONARIOS DO MES--")
for funcionario in funcionarios:

    print(funcionario, "\n--------------")
