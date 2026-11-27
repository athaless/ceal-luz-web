from django.contrib import admin
from .models import Pessoa

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "telefone", "ativo")
    list_filter = ("ativo",)
    search_fields = ("nome", "email", "telefone")
    readonly_fields = ("criado_em", "atualizado_em")

    def has_delete_permission(self, request, obj=None):
        return False
