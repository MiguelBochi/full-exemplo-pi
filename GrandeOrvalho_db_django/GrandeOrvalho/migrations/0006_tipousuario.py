# Generated by Django 4.2.6 on 2023-10-14 22:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("uploader", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("GrandeOrvalho", "0005_alter_animais_idade"),
    ]

    operations = [
        migrations.CreateModel(
            name="TipoUsuario",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "capa",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="uploader.image",
                    ),
                ),
                ("cliente", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="GrandeOrvalho.cliente")),
                (
                    "funcionario",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="GrandeOrvalho.funcionario"),
                ),
                (
                    "user",
                    models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
                ),
            ],
        ),
    ]
