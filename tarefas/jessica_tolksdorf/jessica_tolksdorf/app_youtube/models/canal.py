from django.db import models
from django.core.validators import MinLengthValidator

class Canal(models.Model):
    canal_id = models.CharField(unique=True,
                                verbose_name='ID do Canal',
                                help_text='Formato desejado: UC1000000214',
                                max_length=12,
                                validators=[MinLengthValidator(12)])

    canal_nome = models.CharField(max_length=100,
                                  help_text='Nome',
                                  verbose_name='Nome do Canal')

    canal_inscritos = models.PositiveIntegerField(default=0,
                                                  help_text='Canal Inscritos',
                                                  verbose_name='Quantidade de inscritos no canal')

    def __str__(self):
        return self.canal_nome