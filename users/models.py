#from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import *
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model




#class User(AbstractUser):
    #nome_completo = models.CharField(verbose_name='Nome Completo:', max_length=60, blank=True)
    #idade = models.CharField(verbose_name='Idade:', max_length=15, blank=True)
    #cargo = models.CharField(verbose_name='Cargo:', max_length=100, blank=True)
    #situacao = models.CharField(verbose_name='Situação:', max_length=20, blank=True)
    #niver = models.CharField(verbose_name='Data de Aniversário:', max_length=30, blank=True)
    #conversao = models.CharField(verbose_name='Data de Conversão:', max_length=30, blank=True)
    #batismo = models.CharField(verbose_name='Data de Batismo:', max_length=30, blank=True)
    #Localizacao = models.CharField(verbose_name='Endereço:', max_length=200, blank=True)
    #telefone = models.CharField(verbose_name='Telefone:', max_length=30, blank=True)
    #foto = models.ImageField(verbose_name='Foto', upload_to='D:/', default='/static/midia/10.png')



class iuser(models.Model):
    names = models.CharField(verbose_name='Nome Completo:', max_length=60, blank=True)
    idadi = models.CharField(verbose_name='Idade:', max_length=15, blank=True)
    ocupacao = models.CharField(verbose_name='Cargo:', max_length=100, blank=True)
    estado = models.CharField(verbose_name='Situação:', max_length=20, blank=True)
    aniversario = models.CharField(verbose_name='Data de Aniversário:', max_length=30, blank=True)
    convert = models.CharField(verbose_name='Data de Conversão:', max_length=30, blank=True)
    banho = models.CharField(verbose_name='Data de Batismo:', max_length=30, blank=True)
    casa = models.CharField(verbose_name='Endereço:', max_length=200, blank=True)
    tel = models.CharField(verbose_name='Telefone:', max_length=30, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, null=True)


    def __str__(self):
        return self.names