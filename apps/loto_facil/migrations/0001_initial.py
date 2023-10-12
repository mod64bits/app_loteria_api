# Generated by Django 4.2.6 on 2023-10-11 14:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jsonform.models.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("usuarios", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Bolao",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Criado em"),
                ),
                (
                    "modified",
                    models.DateTimeField(auto_now=True, verbose_name="Modificado em"),
                ),
                (
                    "nome",
                    models.CharField(
                        max_length=150, unique=True, verbose_name="Descrição"
                    ),
                ),
                (
                    "valor",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=8,
                        verbose_name="Valor Jogos",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Concurso",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Criado em"),
                ),
                (
                    "modified",
                    models.DateTimeField(auto_now=True, verbose_name="Modificado em"),
                ),
                (
                    "concurso",
                    models.CharField(
                        max_length=20, unique=True, verbose_name="Concurso"
                    ),
                ),
                ("data_sorteio", models.DateField(verbose_name="Data Sorteio")),
                (
                    "resultado",
                    django_jsonform.models.fields.ArrayField(
                        base_field=django_jsonform.models.fields.ArrayField(
                            base_field=models.PositiveIntegerField(), size=15
                        ),
                        size=1,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Jogos",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Criado em"),
                ),
                (
                    "modified",
                    models.DateTimeField(auto_now=True, verbose_name="Modificado em"),
                ),
                (
                    "descricao",
                    models.CharField(
                        max_length=50, unique=True, verbose_name="Descrição"
                    ),
                ),
                (
                    "jogos",
                    django_jsonform.models.fields.ArrayField(
                        base_field=django_jsonform.models.fields.ArrayField(
                            base_field=models.PositiveIntegerField(), size=None
                        ),
                        size=None,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ResultadoJogos",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Criado em"),
                ),
                (
                    "modified",
                    models.DateTimeField(auto_now=True, verbose_name="Modificado em"),
                ),
                (
                    "jogo",
                    django_jsonform.models.fields.ArrayField(
                        base_field=django_jsonform.models.fields.ArrayField(
                            base_field=models.PositiveIntegerField(), size=15
                        ),
                        size=None,
                    ),
                ),
                (
                    "acertos",
                    django_jsonform.models.fields.ArrayField(
                        base_field=django_jsonform.models.fields.ArrayField(
                            base_field=models.PositiveIntegerField(), size=None
                        ),
                        blank=True,
                        null=True,
                        size=None,
                    ),
                ),
                (
                    "qt_acertos",
                    models.PositiveIntegerField(
                        default=0, verbose_name="QUantidade Acertos"
                    ),
                ),
                (
                    "bolao",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="result_bolao",
                        to="loto_facil.bolao",
                        verbose_name="Bolão",
                    ),
                ),
                (
                    "concurso",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="result_concurso",
                        to="loto_facil.concurso",
                        verbose_name="Concurso",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Premios",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Criado em"),
                ),
                (
                    "modified",
                    models.DateTimeField(auto_now=True, verbose_name="Modificado em"),
                ),
                (
                    "valor",
                    models.DecimalField(
                        decimal_places=2, max_digits=8, verbose_name="Valor Jogos"
                    ),
                ),
                (
                    "quantidade_acertos",
                    models.PositiveIntegerField(
                        default=11, verbose_name="Quantidade de Acertos"
                    ),
                ),
                (
                    "bolao",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="premio_bolao",
                        to="loto_facil.bolao",
                        verbose_name="Bolão",
                    ),
                ),
                (
                    "concurso",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="premio_concurso",
                        to="loto_facil.concurso",
                        verbose_name="Concuro",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="bolao",
            name="concursos",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="bolao_concursos",
                to="loto_facil.concurso",
                verbose_name="Concurso",
            ),
        ),
        migrations.AddField(
            model_name="bolao",
            name="jogos",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="jogos_bolao",
                to="loto_facil.jogos",
                verbose_name="Jogos",
            ),
        ),
        migrations.AddField(
            model_name="bolao",
            name="participantes",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="bolao_participantes",
                to="usuarios.participantes",
                verbose_name="Participantes",
            ),
        ),
        migrations.AddField(
            model_name="bolao",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Usuário",
            ),
        ),
    ]
