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