from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Link(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    publisher = models.ForeignKey('Publisher', blank=True, null=True)
    game = models.ForeignKey('Game', blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        if self.publisher:
            return self.publisher.name + ' > ' + self.name
        elif self.game:
            return self.game.name + ' > ' + self.name
        else:
            return '(empty link)'


@python_2_unicode_compatible
class Publisher(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=2, blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    @property
    def games(self):
        return Game.objects.filter(publisher=self)
    
    @property
    def links(self):
        return Link.objects.filter(publisher=self)


@python_2_unicode_compatible
class Game(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    
    min_players = models.IntegerField(blank=True, null=True)
    max_players = models.IntegerField(blank=True, null=True)
    min_time = models.IntegerField(blank=True, null=True)
    max_time = models.IntegerField(blank=True, null=True)
    
    publisher = models.ForeignKey('Publisher')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    @property
    def links(self):
        return Link.objects.filter(game=self)
    
    @property
    def players(self):
        if self.min_players is None:
            if self.max_players is None:
                return 'Unknown'
            else:
                return 'Up to ' + str(self.max_players)
        
        if self.max_players is None:
            return str(self.min_players) + '+'
        
        if self.min_players == self.max_players:
            return str(self.min_players)
        
        return str(self.min_players) + ' to ' + str(self.max_players)
    
    @property
    def time(self):
        if self.min_time is None:
            if self.max_time is None:
                return 'Unknown'
            else:
                return 'Up to ' + str(self.max_time) + ' minutes'
        
        if self.max_time is None:
            return str(self.min_time) + '+ minutes'
        
        if self.min_time == self.max_time:
            return str(self.min_time) + ' minutes'
        
        return str(self.min_time) + ' to ' + str(self.max_time) + ' minutes'
