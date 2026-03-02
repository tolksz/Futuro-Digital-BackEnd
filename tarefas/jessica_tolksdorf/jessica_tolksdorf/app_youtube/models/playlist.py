from django.db import models
from django.core.validators import MinLengthValidator



class Playlist(models.Model):
    playlist_id = models.CharField(unique=True,
                                   max_length=11,
                                   validators=[MinLengthValidator(11)],
                                   verbose_name='ID da Playlist',
                                   help_text='Formato desejado: PL100000158')

    nome = models.CharField(max_length=255,
                            validators=[MinLengthValidator(1)],
                            verbose_name='Nome da Playlist',
                            help_text='Insira o nome da Playlist')

    def __str__(self):
        return f"{self.playlist_id} - {self.playlist_nome}"