# Generated by Django 4.1.6 on 2023-02-25 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0002_generacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='generacion',
            field=models.ForeignKey(default=8, on_delete=django.db.models.deletion.CASCADE, to='pokemon.generacion'),
        ),
        migrations.AlterField(
            model_name='generacion',
            name='numero_generacion',
            field=models.IntegerField(choices=[(1, 'Primera Generación'), (2, 'Segunda Generación'), (3, 'Tercera Generación'), (4, 'Cuarta Generación'), (5, 'Quinta Generación'), (6, 'Sexta Generación'), (7, 'Séptima Generación'), (8, 'No especificado')]),
        ),
    ]
