# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('busqueda', '0002_distribuidora'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expediente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('rendicion', models.CharField(max_length=255, null=True)),
                ('nota', models.CharField(max_length=255, null=True)),
                ('distribuidora', models.ForeignKey(to='busqueda.Distribuidora')),
            ],
        ),
    ]
