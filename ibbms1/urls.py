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
from users.views import Addizimo, Eddizimo, perfil, addAta, eddAta, pdf_dizimo, atualizar, submit_dados, Ver_Dados, Editar_Dados, login_requirido, sobre, patri

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
    path('requerid/', views.login_requirido, name='burlar_login')
]
