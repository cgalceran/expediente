# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Distribuidora',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Expediente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('rendicion', models.CharField(max_length=255, null=True)),
                ('total', models.IntegerField(default=0)),
                ('apertura', models.DateField()),
                ('nota', models.CharField(max_length=255, null=True, blank=True)),
                ('distribuidora', models.ForeignKey(to='busqueda.Distribuidora')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('origen', models.CharField(max_length=255)),
                ('destino', models.CharField(max_length=255)),
                ('fecha_envio', models.DateTimeField()),
                ('fecha_recepcion', models.DateTimeField(null=True, blank=True)),
                ('expediente', models.ForeignKey(related_name='items', to='busqueda.Expediente')),
            ],
            options={
                'ordering': ['expediente__distribuidora__provincia', 'expediente', '-fecha_recepcion'],
            },
        ),
        migrations.CreateModel(
            name='PermisoExpediente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='provincia',
            name='tema',
            field=models.ManyToManyField(to='busqueda.Tema'),
        ),
        migrations.AddField(
            model_name='permisoexpediente',
            name='temas',
            field=models.ManyToManyField(to='busqueda.Tema'),
        ),
        migrations.AddField(
            model_name='permisoexpediente',
            name='usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='expediente',
            name='tema',
            field=models.ForeignKey(to='busqueda.Tema', null=True),
        ),
        migrations.AddField(
            model_name='distribuidora',
            name='provincia',
            field=models.ForeignKey(to='busqueda.Provincia'),
        ),
    ]
