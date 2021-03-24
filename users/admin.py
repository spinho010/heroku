from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .forms import UserChangeForm, UserCreationForm
from .models import User
from users.models import iuser


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Informações Pessoais", {"fields": ("nome_completo", "idade", "cargo", "situacao", "niver", "conversao", "batismo", "Localizacao", "telefone", "foto")}),
    )


class iuserUser(admin.ModelAdmin):
    list_display = ('names', 'idadi', 'ocupacao', 'estado', 'aniversario', 'convert', 'banho', 'casa', 'tel')

admin.site.register(iuser, iuserUser)