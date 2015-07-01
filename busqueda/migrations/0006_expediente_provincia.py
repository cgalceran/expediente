# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('busqueda', '0005_expediente_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='expediente',
            name='provincia',
            field=models.ForeignKey(to='busqueda.Provincia', null=True),
        ),
    ]
