# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_auto_20150726_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='bgg_url',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='publisher',
            name='bgg_url',
            field=models.URLField(null=True, blank=True),
        ),
    ]
