# Generated by Django 4.2.4 on 2023-09-25 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("compte", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Appel",
            fields=[
                ("num", models.AutoField(primary_key=True, serialize=False)),
                ("date_appel", models.DateTimeField()),
                ("heure_appel", models.TimeField()),
                ("duree_appel", models.IntegerField()),
                ("sujet_appel", models.CharField(max_length=100)),
                ("description_appel", models.TextField()),
                (
                    "etat_appel",
                    models.CharField(
                        choices=[
                            ("EN_ATTENTE", "En attente"),
                            ("EN_COURS", "En cours"),
                            ("TERMINE", "Terminé"),
                        ],
                        max_length=100,
                    ),
                ),
                ("date_enregistrement", models.DateTimeField(auto_now_add=True)),
                (
                    "id_client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="compte.client"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Magasin",
            fields=[
                ("num", models.AutoField(primary_key=True, serialize=False)),
                ("nom", models.CharField(max_length=100)),
                ("adresse", models.CharField(max_length=255)),
                ("code_postal", models.CharField(max_length=5)),
                ("ville", models.CharField(max_length=100)),
                ("date_enregistrement", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Mail",
            fields=[
                ("num", models.AutoField(primary_key=True, serialize=False)),
                ("nom", models.CharField(max_length=100)),
                ("prenom", models.CharField(max_length=100)),
                ("sexe", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("telephone", models.CharField(max_length=10)),
                ("addresse", models.CharField(max_length=255)),
                ("code_postal", models.CharField(max_length=5)),
                ("ville", models.CharField(max_length=100)),
                ("subject", models.CharField(max_length=100)),
                ("message", models.TextField()),
                ("date_enregistrement", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Produit",
            fields=[
                ("num", models.AutoField(primary_key=True, serialize=False)),
                ("nom", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("prix", models.IntegerField()),
                ("image", models.ImageField(upload_to="images")),
                ("fiche_technique", models.FileField(upload_to="documents/")),
                ("date_enregistrement", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Intervention",
            fields=[
                ("num", models.AutoField(primary_key=True, serialize=False)),
                ("date", models.DateTimeField()),
                ("heure", models.TimeField()),
                ("duree", models.IntegerField()),
                ("description", models.TextField()),
                (
                    "etat",
                    models.CharField(
                        choices=[
                            ("EN_ATTENTE", "En attente"),
                            ("EN_COURS", "En cours"),
                            ("TERMINE", "Terminé"),
                        ],
                        max_length=100,
                    ),
                ),
                ("date_enregistrement", models.DateTimeField(auto_now_add=True)),
                (
                    "id_appel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="gestion.appel"
                    ),
                ),
                (
                    "id_technicien",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="compte.technicien",
                    ),
                ),
            ],
        ),
    ]