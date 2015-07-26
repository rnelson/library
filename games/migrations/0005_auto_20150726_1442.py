# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_auto_20150726_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='max_players',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='max_time',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='min_players',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='min_time',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='url',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='country',
            field=models.CharField(max_length=2, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='url',
            field=models.URLField(null=True, blank=True),
        ),
    ]
