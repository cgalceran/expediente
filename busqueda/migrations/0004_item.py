# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('busqueda', '0003_expediente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('origen', models.CharField(max_length=255)),
                ('destino', models.CharField(max_length=255)),
                ('fecha_envio', models.DateTimeField()),
                ('fecha_recepcion', models.DateTimeField()),
                ('expediente', models.ForeignKey(to='busqueda.Expediente')),
            ],
        ),
    ]
