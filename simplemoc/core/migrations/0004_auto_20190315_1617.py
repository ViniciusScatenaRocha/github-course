# Generated by Django 2.1.7 on 2019-03-15 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190315_1323'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='custos',
            options={'ordering': ['restaurante']},
        ),
        migrations.AlterModelOptions(
            name='pedidos',
            options={'ordering': ['pessoa']},
        ),
        migrations.AlterModelOptions(
            name='pessoas',
            options={'ordering': ['nome']},
        ),
    ]