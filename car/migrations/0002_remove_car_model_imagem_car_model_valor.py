# Generated by Django 5.1.4 on 2024-12-27 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car_model',
            name='imagem',
        ),
        migrations.AddField(
            model_name='car_model',
            name='valor',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]
