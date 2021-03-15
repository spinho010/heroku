from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import *



class User(AbstractUser):
    nome_completo = models.CharField(verbose_name='Nome Completo:', max_length=60, blank=True)
    idade = models.CharField(verbose_name='Idade:', max_length=15, blank=True)
    cargo = models.CharField(verbose_name='Cargo:', max_length=100, blank=True)
    situacao = models.CharField(verbose_name='Situação:', max_length=20, blank=True)
    niver = models.CharField(verbose_name='Data de Aniversário:', max_length=30, blank=True)
    conversao = models.CharField(verbose_name='Data de Conversão:', max_length=30, blank=True)
    batismo = models.CharField(verbose_name='Data de Batismo:', max_length=30, blank=True)
    Localizacao = models.CharField(verbose_name='Endereço:', max_length=200, blank=True)
    telefone = models.CharField(verbose_name='Telefone:', max_length=30, blank=True)
    foto = models.ImageField(verbose_name='Foto', upload_to='D:/', default='/static/midia/10.png')
