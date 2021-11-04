"""ibbms1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views
from users.views import Addizimo, Eddizimo, perfil, addAta, eddAta, pdf_dizimo, atualizar, submit_dados, Ver_Dados, Editar_Dados, login_requirido, sobre, patri, fichas, Entradas, EstatutoView, EstatutoView1, EstatutoView2, EstatutoView3, EstatutoView4, EstatutoView5, EstatutoView6, EstatutoView7, EstatutoView8, EstatutoView9, EstatutoView10, EstatutoView11, EstatutoView12, CreatePatri

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("allauth.urls")),
    path("", include("pages.urls", namespace="pages")),
    path("dados/", submit_dados.as_view(), name='addados'),
    path("informacoes/", Ver_Dados.as_view(), name='ver_dados_pessoais'),
    path("dadosedd/<int:pk>/", Editar_Dados.as_view(), name='editar_dados'),
    path("patrimonio/", patri.as_view(), name='patrimonio'),
    path("dizimo/", Addizimo.as_view(), name='dizimo'),
    path("perfil/", perfil.as_view(), name='perfil'),
    path("sobre/", sobre.as_view(), name='sobre'),
    path("relatorios/", addAta.as_view(), name='relatorios'),
    path("atas/", eddAta.as_view(), name='ver_relatorios'),
    path("pdf/", pdf_dizimo.as_view(), name='boot_relatorio'),
    path('atualizacoes/', atualizar.as_view(), name='atualizar'),
    path('requerid/', views.login_requirido, name='burlar_login'),
    path('fichas/', fichas.as_view(), name='fichas'),
    path('entradas/', Entradas.as_view(), name='entradas'),
    path('estatuto/', EstatutoView.as_view(), name='estatuto'),
    path('estatuto/1/', EstatutoView1.as_view(), name='estatuto1'),
    path('estatuto/2/', EstatutoView2.as_view(), name='estatuto2'),
    path('estatuto/3/', EstatutoView3.as_view(), name='estatuto3'),
    path('estatuto/4/', EstatutoView4.as_view(), name='estatuto4'),
    path('estatuto/5/', EstatutoView5.as_view(), name='estatuto5'),
    path('estatuto/6/', EstatutoView6.as_view(), name='estatuto6'),
    path('estatuto/7/', EstatutoView7.as_view(), name='estatuto7'),
    path('estatuto/8/', EstatutoView8.as_view(), name='estatuto8'),
    path('estatuto/9/', EstatutoView9.as_view(), name='estatuto9'),
    path('estatuto/10/', EstatutoView10.as_view(), name='estatuto10'),
    path('estatuto/11/', EstatutoView11.as_view(), name='estatuto11'),
    path('estatuto/12/', EstatutoView12.as_view(), name='estatuto12'),
    path('patrimonioadd/', CreatePatri.as_view(), name='patrimonioadd'),
]