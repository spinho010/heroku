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
from users.views import Addizimo, Eddizimo, perfil, addAta, eddAta, ver_no_pdf, ver_pdf

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("allauth.urls")),
    path("", include("pages.urls", namespace="pages")),
    path("dados/", views.listar_dados),
    path("dados/submit", views.submit_dados),
    path("informacoes/", views.home),
    path("patrimonio/", views.patri),
    path("dizimo/", Addizimo.as_view(), name='dizimo'),
    path("eddizimo/<int:pk>", Eddizimo.as_view(), name='eddizimo'),
    path("perfil/", perfil.as_view(), name='perfil'),
    path("sobre/", views.sobre),
    path("relatorios/", addAta.as_view(), name='relatorios'),
    path("atas/", eddAta.as_view(), name='ver_relatorios'),
    path("relat/<int:pk>/", views.ver_pdf, name='ver_no_pdf'),
]
