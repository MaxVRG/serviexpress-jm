# Generated by Django 5.0.6 on 2024-11-19 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0005_pedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]