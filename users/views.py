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
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
class submit_dados(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('burlar_login')
    model = iuser
    fields = ['names', 'idadi', 'ocupacao', 'estado', 'aniversario', 'convert', 'banho', 'casa', 'tel']
    template_name = 'addados.html'
    success_url = ('/')


class Ver_Dados(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('burlar_login')
    model = iuser
    template_name = 'dados.html'

    def get_queryset(self):
        self.object_list = iuser.objects.filter(usuario=self.request.user)
        return self.object_list


class Editar_Dados(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('burlar_login')
    model = iuser
    fields = ['names', 'idadi', 'ocupacao', 'estado', 'aniversario', 'convert', 'banho', 'casa', 'tel']
    template_name = 'editar_dados.html'
    success_url = ('/')


class patri(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('burlar_login')
    model = dizimo
    template_name = 'patrimonio.html'

################# CRIAR ###################
class Addizimo(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('burlar_login')
    model = dizimo
    fields = ['valor', 'data_entrada', 'usuario']
    template_name = 'dizimo.html'
    success_url = ('/')



################# ATUALIZAR ###################
class Eddizimo(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('burlar_login')
    model = dizimo
    fields = ['valor', 'data_entrada', 'usuario']
    template_name = 'dizimo.html'
    success_url = ('/')


class perfil(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('burlar_login')
    model = dizimo
    template_name = 'perfil.html'

    def get_queryset(self):
        self.object_list = dizimo.objects.filter(usuario=self.request.user)
        return self.object_list



class sobre(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('burlar_login')
    model = dizimo
    template_name = 'desen.html'



class addAta(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('burlar_login')
    model = relatorios
    fields = ['relatorio', 'nome_rela', 'data_relatorio']
    template_name = 'atas.html'
    success_url = ('/')



class eddAta(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('burlar_login')
    model = relatorios
    template_name = 'assem.html'


#####################################

class pdf_dizimo(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('burlar_login')
    model = dizimo
    template_name = 'boot.html'


class atualizar(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('burlar_login')
    model = dizimo
    template_name = 'atualizacoes.html'


def login_requirido(request):
    return render(request, 'requerid.html')

class fichas(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('burlar_login')
    model = iuser
    template_name = 'fichas.html'
