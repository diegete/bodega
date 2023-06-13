# Generated by Django 4.1.2 on 2023-06-13 13:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('productos_api', '0005_carrito_productos'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carrito',
            options={'ordering': ['id'], 'verbose_name': 'Carrito', 'verbose_name_plural': 'Ordenes'},
        ),
        migrations.AddField(
            model_name='carrito',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]