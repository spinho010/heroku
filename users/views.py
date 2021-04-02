from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.models import iuser, dizimo, relatorios
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

# Create your views here.

def home(request):
    usuario = request.user
    iuseer = iuser.objects.filter(usuario=usuario)
    dados = {'iuseers':iuseer}
    return render(request, 'dados.html', dados)


def listar_dados(request):
    return render(request, 'addados.html')


def submit_dados(request):
    if request.POST:
        names = request.POST.get('names')
        idadi = request.POST.get('idadi')
        ocupacao = request.POST.get('ocupacao')
        estado = request.POST.get('estado')
        aniversario = request.POST.get('aniversario')
        convert = request.POST.get('convert')
        banho = request.POST.get('banho')
        casa = request.POST.get('casa')
        tel = request.POST.get('tel')
        iuser.objects.create(names = names,
            idadi = idadi,
            ocupacao = ocupacao,
            estado = estado,
            aniversario = aniversario,
            convert = convert,
            banho = banho,
            casa = casa,
            tel = tel)
    else:
        return HttpResponse('Método inválido para essa operação: {}'.format(request.method))

    return redirect('/')



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