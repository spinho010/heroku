from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from users.models import iuser, dizimo, relatorios
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.
class submit_dados(CreateView):
    model = iuser
    fields = ['names', 'idadi', 'ocupacao', 'estado', 'aniversario', 'convert', 'banho', 'casa', 'tel']
    template_name = 'addados.html'
    success_url = ('/')


class Ver_Dados(ListView):
    model = iuser
    template_name = 'dados.html'

    def get_queryset(self):
        self.object_list = iuser.objects.filter(usuario=self.request.user)
        return self.object_list


def patri(request):
    return render(request, 'patrimonio.html')

################# CRIAR ###################
class Addizimo(CreateView):
    model = dizimo
    fields = ['valor', 'data_entrada', 'usuario']
    template_name = 'dizimo.html'
    success_url = ('/')



################# ATUALIZAR ###################
class Eddizimo(UpdateView):
    model = dizimo
    fields = ['valor', 'data_entrada', 'usuario']
    template_name = 'dizimo.html'
    success_url = ('/')


class perfil(ListView):
    model = dizimo
    template_name = 'perfil.html'

    def get_queryset(self):
        self.object_list = dizimo.objects.filter(usuario=self.request.user)
        return self.object_list



def sobre(request):
    return render(request, 'desen.html')



class addAta(CreateView):
    model = relatorios
    fields = ['relatorio', 'nome_rela', 'data_relatorio']
    template_name = 'atas.html'
    success_url = ('/')



class eddAta(ListView):
    model = relatorios
    template_name = 'assem.html'


#####################################

class pdf_dizimo(ListView):
    model = dizimo
    template_name = 'boot.html'


def atualizar(request):
    return render(request, 'atualizacoes.html')