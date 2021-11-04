from django.contrib import admin
from django.contrib.auth import admin as auth_admin

#from .forms import UserChangeForm, UserCreationForm
#from .models import User
from users.models import iuser
from users.models import dizimo
from users.models import relatorios
from users.models import estatuto
from users.models import patrimonioibb
from users.models import statusItem
from users.models import dispoItem

#@admin.register(User)
#class UserAdmin(auth_admin.UserAdmin):
    #form = UserChangeForm
    #add_form = UserCreationForm
    #model = User
    #fieldsets = auth_admin.UserAdmin.fieldsets + (
        #("Informações Pessoais", {"fields": ("nome_completo", "idade", "cargo", "situacao", "niver", "conversao", "batismo", "Localizacao", "telefone", "foto")}),
    #)


class iuserUser(admin.ModelAdmin):
    list_display = ('names', 'idadi', 'estado', 'aniversario','tel')

admin.site.register(iuser, iuserUser)


class cadDizimo(admin.ModelAdmin):
    list_display = ('usuario', 'data_entrada')

admin.site.register(dizimo, cadDizimo)


class Atas(admin.ModelAdmin):
    list_display = ('nome_rela', 'data_relatorio')

admin.site.register(relatorios, Atas)

class EstatutoAdmin(admin.ModelAdmin):
    list_display = ('estatuto', 'estatuto_data')

admin.site.register(estatuto, EstatutoAdmin)

class PatrimonioAdm(admin.ModelAdmin):
    list_display = ('nome_item', 'quantidade_item', 'status_item', 'dispon_item', 'obs_item', 'doador_item')

admin.site.register(patrimonioibb, PatrimonioAdm)

class Status_Iteem(admin.ModelAdmin):
    list_display = ('StatusI', 'obsI')

admin.site.register(statusItem, Status_Iteem)

class Disponib_Iteem(admin.ModelAdmin):
    list_display = ('DispoI', 'obsII')

admin.site.register(dispoItem, Disponib_Iteem)