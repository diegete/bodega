# Generated by Django 4.1.2 on 2023-06-20 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos_api', '0007_producto_fecha'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carrito',
            options={},
        ),
        migrations.AlterField(
            model_name='producto',
            name='idProducto',
            field=models.IntegerField(max_length=20, primary_key=True, serialize=False, verbose_name='idProducto'),
        ),
    ]