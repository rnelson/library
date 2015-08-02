# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0008_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='bgg_url',
        ),
        migrations.RemoveField(
            model_name='game',
            name='url',
        ),
        migrations.RemoveField(
            model_name='publisher',
            name='bgg_url',
        ),
        migrations.RemoveField(
            model_name='publisher',
            name='url',
        ),
    ]
