import django
import csv
from datetime import datetime
from manage import *
import contextlib, io

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jessica_tolksdorf.settings")
django.setup()

from app_youtube.models import Video, Canal, Categoria, Playlist

saida = io.StringIO()
with contextlib.redirect_stdout(saida):
    main()


def clean_int(valor):
    try:
        return int(float(valor.strip()))
    except (TypeError, ValueError):
        return 0


def clean_duracao(valor):
    try:
        return datetime.strptime(valor, "%H:%M:%S").time()
    except Exception:
        return None


def clean_data(valor):
    try:
        return datetime.strptime(valor, "%Y-%m-%d").date()
    except Exception:
        return None

VISIBILIDADE_MAP = {
    "PUBLICO": "PUBLICO",
    "PÚBLICO": "PUBLICO",
    "PRIVADO": "PRIVADO",
    "NAO_LISTADO": "NAO_LISTADO",
    "NÃO_LISTADO": "NAO_LISTADO",
}



with open("nao_normalizado.csv", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    erros = 0

    for linha_num, linha in enumerate(leitor, start=2):
        try:
            canal, _ = Canal.objects.get_or_create(
                canal_id=(linha.get("canal_id") or "").strip(),
                defaults={
                    "canal_nome": (linha.get("canal_nome") or "").strip(),
                    "canal_inscritos": clean_int(linha.get("canal_inscritos")),
                }
            )

            playlist = None
            if linha.get("playlist_id") and linha.get("playlist_nome"):
                playlist, _ = Playlist.objects.get_or_create(
                    playlist_id=(linha["playlist_id"] or None).strip(),
                    defaults={"nome": (linha["playlist_nome"] or None).strip()}
                )

            categorias_nomes = {
                c.strip().lower()
                for c in (linha.get("categorias").strip() or "").split(";")
                if c.strip()
            }

            if not categorias_nomes:
                raise ValueError("Vídeo sem categorias")

            categorias_objs = [
                Categoria.objects.get_or_create(nome=nome)[0]
                for nome in categorias_nomes
            ]
            visibilidade_raw = (linha.get("visibilidade") or "").strip().upper()
            video = Video.objects.create(
                video_id=(linha.get("video_id") or None).strip(),
                url=(linha.get("url") or None).strip(),
                titulo=(linha.get("titulo") or None).strip(),
                likes=clean_int(linha.get("likes")),
                dislikes=clean_int(linha.get("dislikes")),
                salvos=clean_int(linha.get("salvos")),
                downloads=clean_int(linha.get("downloads")),
                duracao=clean_duracao(linha.get("duracao")),
                comentarios=clean_int(linha.get("comentarios")),
                qualidade_px=max(clean_int(linha.get("qualidade_px")), 144),
                palavras_chave=[
                    p.strip().lower()
                    for p in ((linha.get("palavras_chave") or None).strip()).split(";")
                    if p.strip()
                ],
                descricao=(linha.get("descricao") or "").strip(),
                data_postagem=clean_data(linha.get("data_postagem")),
                visibilidade=(VISIBILIDADE_MAP.get(visibilidade_raw) or None),
                idioma=(linha.get("idioma") or "").strip() or None,
                canal=canal,
                playlist=playlist
            )

            video.categorias.set(categorias_objs)

        except Exception as e:
            print(f"Linha {linha_num} com exceção: {e}")
            erros += 1

if erros:
    print(f"Importação finalizada com {erros} exceções.")
else:
    print("Importação finalizada com sucesso.")