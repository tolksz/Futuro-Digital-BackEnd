from django.db.models import QuerySet, Count, Sum, Avg, F, FloatField, ExpressionWrapper
from .base_manager import BaseManager

from datetime import date
from typing import List, Tuple

class VideoManager(BaseManager):
    def publicos(self) -> QuerySet['Video']:
        return self.filter(visibilidade="PUBLICO")

    def privados(self) -> QuerySet['Video']:
        return self.filter(visibilidade="PRIVADO")

    def videos_do_canal(self, canal_youtube_id: str) -> QuerySet['Video']:
        return self.filter(canal__canal_id=canal_youtube_id)

    def videos_da_playlist(self, playlist_youtube_id: str) -> QuerySet['Video']:
        return self.filter(playlist__playlist_id=playlist_youtube_id)

    def sem_playlist(self) -> QuerySet['Video']:
        return self.filter(playlist__isnull=True)

    def videos_da_categoria(self, categoria_nome: str) -> QuerySet['Video']:
        return self.filter(categorias__nome__iexact=categoria_nome)

    def com_qualidade_minima(self, qualidade_min_px: int) -> QuerySet['Video']:
        return self.filter(qualidade_px__gte=qualidade_min_px)

    def postados_entre(self, inicio: date, fim: date) -> QuerySet['Video']:
        return self.filter(data_postagem__range=(inicio, fim))

    def top_por_likes(self, n: int = 10, somente_publicos: bool = True) -> QuerySet['Video']:
        qs = self
        if somente_publicos:
            qs = qs.publicos()
        return qs.order_by("-likes")[:n]

    def dislikes_maior_que(self, minimo: int) -> QuerySet['Video']:
        return self.filter(dislikes__gt=minimo)

    def com_taxa_dislike_minima(self, taxa_min: float, likes_min: int = 1000) -> QuerySet['Video']:
        return (
            self.filter(likes__gte=likes_min)
            .annotate(
                taxa_dislike=ExpressionWrapper(
                    F("dislikes") * 1.0 / F("likes"),
                    output_field=FloatField()
                )
            )
            .filter(taxa_dislike__gte=taxa_min)
        )

    def buscar_por_palavra_chave(self, termo: str) -> QuerySet['Video']:
        return self.filter(palavras_chave__icontains=termo)

    def top_por_comentarios(self, n: int = 10) -> QuerySet['Video']:
        return self.order_by("-comentarios")[:n]

    def ranking_canais_por_qtd_videos(self, limit: int = 10) -> List[Tuple[str, int]]:
        return list(
            self.values("canal__canal_nome")
            .annotate(total_videos=Count("id"))
            .order_by("-total_videos")[:limit]
            .values_list("canal__canal_nome", "total_videos")
        )

    def ranking_canais_por_soma_likes(self, limit: int = 10) -> List[Tuple[str, int]]:
        return list(
            self.values("canal__canal_nome")
            .annotate(total_likes=Sum("likes"))
            .order_by("-total_likes")[:limit]
            .values_list("canal__canal_nome", "total_likes")
        )

    def ranking_canais_por_media_comentarios(self, limit: int = 10) -> List[Tuple[str, float]]:
        return list(
            self.values("canal__canal_nome")
            .annotate(media_comentarios=Avg("comentarios"))
            .order_by("-media_comentarios")[:limit]
            .values_list("canal__canal_nome", "media_comentarios")
        )

    def stats_por_qualidade(self) -> List[Tuple[int, int, float]]:
        return list(
            self.values("qualidade_px")
            .annotate(
                total_videos=Count("id"),
                likes_medio=Avg("likes")
            )
            .order_by("qualidade_px")
            .values_list("qualidade_px", "total_videos", "likes_medio")
        )

    def stats_por_idioma(self) -> List[Tuple[str, int, float]]:
        return list(
            self.values("idioma")
            .annotate(
                total_videos=Count("id"),
                comentarios_medio=Avg("comentarios")
            )
            .order_by("idioma")
            .values_list("idioma", "total_videos", "comentarios_medio")
        )

    def top_categorias_por_videos(self, n: int = 10) -> List[Tuple[str, int]]:
        return list(
            self.values("categorias__nome")
            .annotate(total_videos=Count("id"))
            .order_by("-total_videos")[:n]
            .values_list("categorias__nome", "total_videos")
        )

    def top_por_engajamento(self, n: int = 20, somente_publicos: bool = True) -> QuerySet['Video']:
        qs = self

        if somente_publicos:
            qs = qs.filter(visibilidade="PUBLICO")

        return (
            qs.annotate(
                engajamento=F("likes") + F("comentarios") + F("salvos")
            )
            .order_by("-engajamento")[:n]
        )