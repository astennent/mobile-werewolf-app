from django.db import models
from django.contrib.auth.models import User

class Badge(models.Model):
    name = models.CharField(max_length=63)
    description = models.CharField(max_length=127)
    points = models.IntegerField()


class Game(models.Model):
    start_time = models.DateField(auto_now_add=True) #use current time.
    cycle_length = models.IntegerField(default=1800) #12 hours
    in_progress = models.BooleanField(default=True)


class Account(models.Model):
    user = models.ForeignKey(User, related_name='+') #use the django admin user
    badges = models.ManyToManyField(Badge, blank=True)
    experience = models.PositiveIntegerField(default=0)


class Player(models.Model):
    account = models.ForeignKey(Account)
    game = models.ForeignKey(Game)
    is_dead = models.BooleanField(default=False)
    is_wolf = models.BooleanField(default=False)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    vote = models.ForeignKey('self', null=True, blank=True) #reset to null at the start of the day cycle.


class Kill(models.Model):
    killer = models.ForeignKey(Player, related_name="kill-killer")
    victim = models.ForeignKey(Player, related_name="kill-victim")
    latitude = models.FloatField() #these are victim's coordinates
    longitude = models.FloatField()
    time = models.DateField(auto_now_add=True)
