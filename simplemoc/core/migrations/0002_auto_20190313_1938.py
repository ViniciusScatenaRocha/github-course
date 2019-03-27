# Generated by Django 2.1.7 on 2019-03-13 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedidos',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='pessoas',
            name='tamanho',
        ),
        migrations.AddField(
            model_name='pedidos',
            name='pessoa',
            field=models.ForeignKey(default='7', on_delete=django.db.models.deletion.CASCADE, to='core.Pessoas'),
        ),
        migrations.AddField(
            model_name='pedidos',
            name='restaurante',
            field=models.ForeignKey(default='8', on_delete=django.db.models.deletion.CASCADE, to='core.Custos'),
        ),
        migrations.AddField(
            model_name='pessoas',
            name='altura',
            field=models.DecimalField(decimal_places=2, default='1', max_digits=4),
        ),
        migrations.AlterField(
            model_name='custos',
            name='comida',
            field=models.CharField(default='5', max_length=30),
        ),
        migrations.AlterField(
            model_name='custos',
            name='custos',
            field=models.DecimalField(decimal_places=2, default='6', max_digits=5),
        ),
        migrations.AlterField(
            model_name='custos',
            name='restaurante',
            field=models.CharField(default='4', max_length=50),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='comida',
            field=models.CharField(default='10', max_length=30),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='dia',
            field=models.DateTimeField(default='9', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='pessoas',
            name='cidade',
            field=models.CharField(default='3', max_length=30),
        ),
        migrations.AlterField(
            model_name='pessoas',
            name='idade',
            field=models.DecimalField(decimal_places=2, default='2', max_digits=8),
        ),
        migrations.AlterField(
            model_name='pessoas',
            name='nome',
            field=models.CharField(default='0', max_length=30),
        ),
    ]