from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils.deconstruct import deconstructible

# decorator utilizado para tornar a classe "serializavel" para as migracoes
# ou seja, como construir e reconstruir essas classes
@deconstructible
class CodValidator:

    # simples inicialização da classe validadora
    def __init__(self, cod="0000000000"):
        self.code = cod

    # neste método é implementado o validador
    def __call__(self, valor):
        if valor == self.code:
            raise ValidationError(
                _("Valor inválido"),
                params={"valor": valor},
            )
    # método necessário para tornar a classe serializável
    def __eq__(self, other):
        return (
            isinstance(other, CodValidator)
            and self.code == other.code
        )
