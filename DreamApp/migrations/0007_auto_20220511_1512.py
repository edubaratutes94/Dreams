# Generated by Django 3.1.7 on 2022-05-11 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DreamApp', '0006_auto_20220511_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='tipo_servicio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='DreamApp.service', verbose_name='Tipo de Servicio'),
        ),
    ]
