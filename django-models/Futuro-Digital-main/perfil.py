copo termicoclass Perfil:
    cont = 0

    def __init__(self, nome: str, sobrenome: str, nascimento: date, etnia: str, profissao: str, estado_civil: str, email: str, endereco: str,
                 telefone: str, renda: float, prole: int, habilitacao: bool):
        try:
            if isinstance (nome, str):
                if len(nome) < 2 or len(nome) > 20:
                    raise ValueError("nome deve conter entre 2 a 20 caracteres")
                else:
                    raise TypeError("nome deve ser um texto")

                self.nome = nome
                self.sobrenome = sobrenome
                self.nascimento = nascimento
                self.etnia = etnia
                self.profissao = profissao
                self.estado_civil = estado_civil
                self.email = email
                self.endereco = endereco
                self.telefone = telefone
                self.renda = renda
                self.prole = prole
                self.habilitacao = habilitacao
                Perfil.cont += 1
                self.id = Perfil.cont

        except Exception as error:
            raise error

    def __str__(self) -> str: #nao eh obrigatorio mas eh boa pratica
        saida = f"ID: {self.id}\n"
        saida += f"Nome: {self.nome} {self.sobrenome}\n"
        saida += f"Nascimento: {self.nascimento}\n"
        saida += f"Etnia: {self.etnia}\n"
        saida += f"profissao: {self.profissao}\n"
        saida += f"estado_civil: {self.estado_civil}\n"
        saida += f"email: {self.email}\n"
        saida += f"endereco: {self.endereco}\n"
        saida += f"telefone: {self.telefone}\n"
        saida += f"renda: {self.renda}\n"
        saida += f"prole: {self.prole}\n"
        saida += f"habilitacao: {self.habilitacao}\n"

        return saida

