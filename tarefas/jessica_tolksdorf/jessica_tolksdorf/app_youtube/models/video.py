from app_youtube.enumerations.visibilidade import Visibilidade
from app_youtube.managers import VideoManager
from app_youtube.models.playlist import Playlist
from app_youtube.models.categoria import Categoria
from app_youtube.models.canal import Canal
from app_youtube.models.base_model import BaseModel
from django.utils.timezone import now
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models




class Video(BaseModel):
    video_id = models.CharField(unique=True,
                                max_length=11,
                                validators=[MinLengthValidator(11)],
                                help_text='ID do Vídeo',
                                verbose_name='Exemplo: GboIRoL3u6a')

    canal = models.ForeignKey(Canal, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria, verbose_name='Categorias')
    playlist = models.ForeignKey(Playlist, on_delete=models.SET_NULL, null=True, blank=True)
    url = models.URLField(unique=True, help_text='Link do video', verbose_name='URL')
    titulo = models.CharField(max_length=100, help_text='Titulo', verbose_name='Titulo')
    likes = models.PositiveIntegerField(default=0, help_text='Quantidade de likes', verbose_name='Likes')
    dislikes = models.PositiveIntegerField(default=0, help_text='Quantidade de dislikes', verbose_name='Dislikes')
    salvos = models.PositiveIntegerField(default=0, help_text='Quantidade de salvos', verbose_name='Salvos')
    downloads = models.PositiveIntegerField(default=0, help_text='Quantidade de downloads', verbose_name='Downloads')
    duracao = models.TimeField(auto_now=False, auto_now_add=False, verbose_name='Durção', help_text='Duração do vídeo')
    comentarios = models.PositiveIntegerField(default=0, blank=True, null=True,
                                              help_text='Quantidade de comentários do vídeo', verbose_name='Comentários')
    qualidade_px = models.PositiveIntegerField(default=144, validators=[MinValueValidator(144)], verbose_name='Resolução',
                                               help_text='Resolução do vídeo')
    palavras_chave = models.JSONField(default=list, help_text='Palavras Chave', verbose_name='Palavras Chave separadas por ;')
    descricao = models.TextField(max_length=5000, help_text='Descrição', verbose_name='Descrição', blank=True, null=True) # Valor máximo de 5000 caracteres segundo YouTube
    data_postagem = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Data da Postagem', help_text='Data da Postagem')
    visibilidade = models.CharField(choices=Visibilidade, help_text='Visibilidade', max_length=100, verbose_name='Visibilidade')
    idioma = models.CharField(max_length=5, help_text='Idioma', verbose_name='Formato desejado: pt-BR ou pt', blank=True, null=True) # Pode ser vazio para vídeos sem falas.

    objects = VideoManager()

    def __str__(self):
        return self.titulo

    def clean(self):
        super().clean()
        if self.data_postagem > now().date():
            raise ValidationError(
                {"data_postagem": f"Não pode exceder hoje ({now().date()})"}
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)