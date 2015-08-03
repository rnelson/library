from __future__ import unicode_literals
from django.conf.urls import url, patterns
from games import views

urlpatterns = patterns(
    '',
    url('^/?$', views.index, name='index_games'),
    url(r'^about', views.about, name='about'),
    url(r'^publishers', views.publishers, name='index_publishers'),
    url(r'^publisher/(?P<slug>\w+)/?$', views.publisher_details),
    url(r'(?P<slug>\w+)', views.game_details),
)