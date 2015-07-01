# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('busqueda', '0004_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='expediente',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
