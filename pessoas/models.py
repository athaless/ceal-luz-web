from django.db import models

class Pessoa(models.Model):
    nome = models.CharField("Nome completo", max_length=150)
    email = models.EmailField("E-mail", blank=True)
    telefone = models.CharField("Telefone", max_length=30, blank=True)
    data_nascimento = models.DateField("Data de nascimento", null=True, blank=True)
    ativo = models.BooleanField("Ativo", default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["nome", "pk"]
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

    def __str__(self):
        return self.nome
