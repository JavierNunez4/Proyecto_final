# Generated by Django 4.2.4 on 2023-11-02 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0003_alter_solicitudes_fecha_de_solicitud'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitudes',
            name='rut',
            field=models.IntegerField(default=0),
        ),
    ]
