# Generated by Django 4.1.6 on 2023-02-25 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0003_pokemon_generacion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='generacion',
        ),
    ]