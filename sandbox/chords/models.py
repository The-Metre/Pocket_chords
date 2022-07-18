from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

class Artist(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Artist: {self.name}."

class Track(models.Model):
    name = models.CharField(max_length=255, blank=False)
    text = models.CharField(max_length=2000, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    creator = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='created_track')

    def __str__(self):
        return f'Track: {self.name} by {self.creator}'

class Chords(models.Model):
    name = models.CharField(max_length=255, blank=False)
    symbol = models.CharField(max_length=255, blank=False)
    steps = models.CharField(max_length=255, blank=False)
    notes = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return f'{self.name} chord'

class Watchlist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='added_to_watchlist')
    track = models.ForeignKey(Track, on_delete=models.CASCADE, related_name='added_to_watchlist')

    def __str__(self):
        return f'{self.user} added {self.track} to watchlist'