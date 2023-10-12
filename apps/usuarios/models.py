from django.db import models
from django.conf import settings


class Participantes(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Usuário')
    nome = models.CharField('nome', max_length=150)
    whatsapp = models.CharField("Whatsapp", max_length=30)


    def __str__(self):
        return self.nome
