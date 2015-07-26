from __future__ import unicode_literals
from django.conf.urls import url, include, patterns
from django.views.generic import TemplateView
from games import views

urlpatterns = patterns(
    '',
    url('^/?$', views.index, name='index_games'),
    url(r'^about', views.about, name='about'),
    url(r'^publishers', views.publishers, name='index_publishers'),
    url(r'^publisher/(?P<slug>\w+)/?$', views.publisher_details),
    url(r'(?P<slug>\w+)', views.game_details),
#     url(r'docs/', include(patterns(
#         url(r'/?', TemplateView.as_view(template_name='api2/index.html')),
#     ))),
)