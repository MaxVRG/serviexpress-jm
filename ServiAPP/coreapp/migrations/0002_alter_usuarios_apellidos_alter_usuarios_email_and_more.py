# Generated by Django 5.0.6 on 2024-11-12 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='apellidos',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='nombre_usuario',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='run',
            field=models.CharField(max_length=12),
        ),
    ]