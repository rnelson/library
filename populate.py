#!/usr/bin/env python
"""
 Populates the database with some test data
"""
from os import unlink, environ
from os.path import join, dirname, abspath
from subprocess import call

dragons = dirname(abspath(__file__))

def add_publisher(slug, name, country=None, url=None):
    p = Publisher.objects.get_or_create(slug=slug, name=name, country=country, url=url)[0]
    return p

def add_game(slug, name, publisher, description=None, url=None, min_players=None, max_players=None, min_time=None, max_time=None):
    g = Game.objects.get_or_create(slug=slug, name=name, publisher=publisher, description=description, url=url, min_players=min_players, max_players=max_players, min_time=min_time, max_time=max_time)[0]
    return g

def populate():
    pOne = add_publisher('one', 'Publisher One', 'US')
    pTwo = add_publisher('two', 'Publisher Two', url='http://geocities.com/pubtwo')
    pSix = add_publisher('six', 'Super Duper Game Publisher', country='AU', url='http://six.co.uk/games/au')
    
    add_game('one', 'First Game', pOne, min_players=2, max_players=4)
    add_game('two', 'Second Game', pTwo, min_players=5, min_time=60, max_time=60)
    add_game('three', 'Third Game', pSix, description='It\'s a game!', url='http://six.co.uk/games/au/three.cfm', max_players=10, min_time=15)
    add_game('four', 'Fourth Game', pSix, min_time=45, max_time=90)
    add_game('five', 'Fifth Game', pTwo, min_time=120)
    add_game('six', 'Sixth Game', pOne, max_time=30)
    add_game('seven', 'Seventh Game', pSix)

if __name__ == '__main__':
    print 'Populating the database...'
    
    dbfile = join(dragons, 'db.sqlite3')
    manage = join(dragons, 'manage.py')
    
    # Remove the database file
    unlink(dbfile)
    
    # Run migrations
    call(['python', manage, 'migrate'])
    
    # Add an admin user
    call(['python', manage, 'createsuperuser'])
    
    # Set up Django
    environ.setdefault('DJANGO_SETTINGS_MODULE', 'library.settings')
    import django
    django.setup()
    
    # Import our dummy data
    from games.models import Game, Publisher
    populate()