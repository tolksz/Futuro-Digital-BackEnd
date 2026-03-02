from datetime import date


class Funcionario:

    def __init__(self, nome: str, nascimento: date, cargo: str, departamento: str, admissao: date, regime_trabalho: int,
                 valor_hora: float):

        self.nome = nome
        self.nascimento = nascimento
        self.cargo = cargo
        self.departamento = departamento
        self.admissao = admissao
        self.regime_trabalho = regime_trabalho
        self.valor_hora = valor_hora

    def __str__(self):
        return (f"Nome: {self.nome} \nCargo: {self.cargo} \nDepartamento: {self.departamento}")

                # f"\nAdmissão: {self.admissao}"
                # f"\nRegime de Trabalho: {self.regime_trabalho} \nValor da Hora: {self.valor_hora}")


    def calcular_salario(self, mes):
        salario = self.regime_trabalho * self.valor_hora * mes
        if salario < 5000:
            return salario - (salario/100*8) - (salario/100)
        elif salario < 7000:
            return salario - (salario/100*8) - (salario/100) - (salario/100*12.5)
        elif salario < 50000:
            return salario - (salario/100*8) - (salario/100) - (salario/100*27.5)
        else:
            return salario - salario - (salario/100*8) - (salario/100) - (salario/100*37.5)


    def parabenizar_funcionario(self):
        print(f"Parabens! Feliz aniversário, que dia mais feliz! - XUXA")
