from django.db import models

class SelfieHistorica(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='thumbs/', blank=True, null=True)

    def __str__(self):
        return self.nome
