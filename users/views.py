from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.models import iuser
# Create your views here.

def home(request):
    iuseer = iuser.objects.all()
    response = {'iuseer':iuseer}
    return render(request, 'dados.html', response)


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

