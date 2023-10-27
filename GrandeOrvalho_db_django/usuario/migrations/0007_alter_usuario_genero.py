# Generated by Django 4.2.6 on 2023-10-27 14:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("usuario", "0006_usuario_capa_usuario_genero_usuario_idade_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usuario",
            name="genero",
            field=models.IntegerField(choices=[(1, "Macho"), (2, "Fêmea")], default=1, verbose_name="Gênero"),
        ),
    ]
