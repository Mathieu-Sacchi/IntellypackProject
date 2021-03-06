# Generated by Django 3.1.4 on 2021-01-08 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERP', '0002_auto_20210108_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='siren',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='collaborateurs',
            name='numero_collaborateur',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='dossiers',
            name='loyer',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='dossiers',
            name='montant',
            field=models.CharField(max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='dossiers',
            name='siren_fournisseur',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
