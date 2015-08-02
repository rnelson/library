from __future__ import unicode_literals
from django.contrib import admin
from games.models import Game, Publisher, Link

# Register your models here.
admin.site.register([Game, Publisher, Link])