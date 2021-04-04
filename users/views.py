from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.models import iuser, dizimo, relatorios
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

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



def some_view(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(200, 750, "RELATORIO FINANCEIRO - IBBMS 2021")
    p.drawString(70, 650, "Nome: {}  Data: {}")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='relatorio_financeiro.pdf')