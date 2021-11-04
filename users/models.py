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


    
class dizimo(models.Model):
    valor = models.CharField(verbose_name='Valor da Entrada:',max_length=50, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    data_entrada = models.CharField(verbose_name='Data da Entrada:', max_length=50, blank=True)



class relatorios(models.Model):
    nome_rela = models.CharField(verbose_name='Nome do Relatorio:', max_length=100, blank=True)
    relatorio = models.TextField(verbose_name='Relatório:', max_length=900, blank=True)
    data_relatorio = models.CharField(verbose_name='Data do Relatorio:', max_length=50, blank=True)


class estatuto(models.Model):
    estatuto = models.TextField(verbose_name='Artigos', max_length=1000000, blank=True, null=True)
    estatuto_data = models.CharField(verbose_name='Data Estatuto', max_length=100, blank=True, null=True)



class statusItem(models.Model):
    StatusI = models.CharField(verbose_name='Status do item:', max_length=60, null=True, blank=True)
    obsI = models.CharField(verbose_name='Obs Item: ', max_length=60, null=True, blank=True)

    def __str__(self):
            return "{}".format(self.StatusI)



class dispoItem(models.Model):
    DispoI = models.CharField(verbose_name='Disponibilidade do item:', max_length=60, null=True, blank=True)
    obsII = models.CharField(verbose_name='Obs Item: ', max_length=60, null=True, blank=True)

    def __str__(self):
            return "{}".format(self.DispoI)



class patrimonioibb(models.Model):
    nome_item = models.CharField(verbose_name='Nome: ', max_length=100, blank=True, null=True)
    quantidade_item = models.IntegerField(verbose_name='Quantidade: ', blank=True, null=True)
    status_item = models.ForeignKey(statusItem, max_length=100, null=True, on_delete=models.PROTECT)
    dispon_item = models.ForeignKey(dispoItem, max_length=100, null=True, on_delete=models.PROTECT)
    obs_item = models.CharField(verbose_name='Observações: ', max_length=100, blank=True, null=True)
    doador_item =models.CharField(verbose_name='Doado por: ', max_length=100, blank=True, null=True)

    def __str__(self):
            return "{}".format(self.nome_item)

