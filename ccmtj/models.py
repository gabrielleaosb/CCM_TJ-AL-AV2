from django.db import models

class SelfieHistorica(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='thumbs/', blank=True, null=True)
    personagemSelfie = models.ImageField(upload_to='personagemSelfie', blank=True, null=True)

    def __str__(self):
        return self.nome


class AudioDescricao(models.Model):
    titulo = models.CharField(max_length=255)
    audio = models.FileField(upload_to='audios/')

    def __str__(self):
        return self.titulo


# NOVO MODELO PARA EXPOSIÇÕES
class Exposicao(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('image', 'Imagem'),
        ('video', 'Vídeo'),
    ]
    
    titulo = models.CharField("Título", max_length=200)
    descricao = models.TextField("Descrição")
    
    media_type = models.CharField(
        "Tipo de Mídia",
        max_length=40,
        choices=MEDIA_TYPE_CHOICES,
        default='image'
    )
    
    imagem = models.ImageField(
        "Imagem",
        upload_to='exposicoes/',
        blank=True,
        null=True,
        help_text="Envie uma imagem se selecionou 'Imagem' como tipo de mídia"
    )
    
    video_url = models.CharField(
        "ID do Vídeo do YouTube",
        max_length=50,
        blank=True,
        null=True,
        help_text="Insira apenas o ID do vídeo (ex: lETYY1fCXuE) se selecionou 'Vídeo' como tipo de mídia"
    )

    class Meta:
        verbose_name = "Exposição"
        verbose_name_plural = "Exposições"

    def __str__(self):
        return self.titulo
