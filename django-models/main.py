from perfil import Perfil
from datetime import date


perfis = [Perfil(nome="bernardinho", sobrenome="da silva", nascimento="18/10/1980", etnia="nao declarado", profissao="estudante",
                    estado_civil="solteiro", email="gmail.com", endereco="rua tal", telefone="5555", renda="1000",
                     prole="0", habilitacao="false"),
        Perfil(nome="carlos", sobrenome="pereira", nascimento="20/12/1979", etnia="branco", profissao="engenheiro",
                    estado_civil="casado", email="a@gmail.com", endereco="rua tal", telefone="5555", renda="1000",
                    prole="3", habilitacao="false"),
        Perfil(nome="alice", sobrenome="maria", nascimento="03/06/2005", etnia="branco", profissao="marceneiro",
                    estado_civil="namorando", email="mali@gmail.com", endereco="rua x", telefone="5555", renda="1000",
                    prole=0, habilitacao="True")]

print(10*"-"+"PERFIS CADASTRADOS"+10*"-")
for perfil in perfis:
    print(perfil)


print(10*"-"+"MARCENEIRES CADASTRADOS"+10*"-")
for perfil in perfis:
    if "MARCENEIR" in perfil.profissao.upper():
        print(f"{perfil.nome} {perfil.sobrenome}")
        print(5*"-")