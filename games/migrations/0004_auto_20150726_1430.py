# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_auto_20150725_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='max_players',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='max_time',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='min_players',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='min_time',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='game',
            name='url',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='country',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='url',
            field=models.URLField(null=True),
        ),
    ]
