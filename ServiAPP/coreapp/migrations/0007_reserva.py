# Generated by Django 5.0.6 on 2024-11-19 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0006_producto_precio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run', models.CharField(max_length=12)),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('fecha_reserva', models.DateField()),
                ('hora_reserva', models.TimeField()),
            ],
        ),
    ]
