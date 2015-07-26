# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_auto_20150726_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='image_url',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='publisher',
            name='image_url',
            field=models.URLField(null=True, blank=True),
        ),
    ]
