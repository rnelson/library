from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render_to_response
from games.models import Game, Publisher
from django.template.context import RequestContext
from django.utils import formats


# Create your views here.
def index(request):
    games = Game.objects.all().order_by('name')
    context = RequestContext(request)
    return render_to_response('games/index_games.html', {'games': games}, context)


def about(request):
    context = RequestContext(request)
    return render_to_response('games/about.html', {}, context)


def publishers(request):
    publishers = Publisher.objects.all().order_by('-updated_at')
    context = RequestContext(request)
    return render_to_response('games/index_publishers.html', {'publishers': publishers}, context)


def game_details(request, slug):
    game = get_object_or_404(Game, slug=slug)
    added_date = formats.date_format(game.created_at, 'SHORT_DATE_FORMAT')
    context = RequestContext(request)
    return render_to_response('games/details.html', {'game': game, 'added_date': added_date}, context)


def publisher_details(request, slug):
    publisher = get_object_or_404(Publisher, slug=slug)
    games = Game.objects.filter(publisher=publisher)
    context = RequestContext(request)
    return render_to_response('games/publisher.html', {'publisher': publisher, 'games': games}, context)
