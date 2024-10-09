# Generated by Django 5.1.2 on 2024-10-09 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VENTAS',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Precio')),
                ('vendedor', models.CharField(max_length=80, verbose_name='Vendedor')),
                ('impuestos', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Impuestos')),
                ('comprador', models.CharField(max_length=80, verbose_name='Comprador')),
                ('fecha', models.DateTimeField(verbose_name='Fecha')),
            ],
        ),
    ]
