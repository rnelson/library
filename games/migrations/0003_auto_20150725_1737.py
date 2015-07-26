# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20150725_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='max_players',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='max_time',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='min_players',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='min_time',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='country',
            field=models.CharField(max_length=2, blank=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
