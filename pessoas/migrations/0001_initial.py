from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Pessoa",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=150, verbose_name="Nome completo")),
                ("email", models.EmailField(blank=True, max_length=254, verbose_name="E-mail")),
                ("telefone", models.CharField(blank=True, max_length=30, verbose_name="Telefone")),
                ("data_nascimento", models.DateField(blank=True, null=True, verbose_name="Data de nascimento")),
                ("ativo", models.BooleanField(default=True, verbose_name="Ativo")),
                ("criado_em", models.DateTimeField(auto_now_add=True)),
                ("atualizado_em", models.DateTimeField(auto_now=True)),
            ],
            options={"ordering": ["nome", "pk"], "verbose_name": "Pessoa", "verbose_name_plural": "Pessoas"},
        ),
    ]
