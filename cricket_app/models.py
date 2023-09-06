from django.db import models
from django_extensions.db.models import TimeStampedModel


class Team(models.Model):
    name = models.CharField(max_length=30)
    logo = models.ImageField(upload_to='team_logo', default='team_logo/team_logo.jpg')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class Player(models.Model):
    FORMAT = (
        ('T20', 'T20'),
        ('ODI', 'ODI'),
        ('Test', 'Test'),
        ('All Formats', 'All Formats')
    )
    TYPE = (
        ('Batter', 'Batter'),
        ('Bowler', 'Bowler'),
        ('WicketKeeper Batter', 'WicketKeeper Batter'),
        ('All Rounder', 'All Rounder')
    )
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='player_team')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='player_images', default='player_images/default_player_image.jpg')
    jersey_no = models.PositiveSmallIntegerField()
    format = models.CharField(max_length=11, choices=FORMAT)
    type = models.CharField(max_length=19, choices=TYPE)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Squad(models.Model):
    name = models.CharField(max_length=30)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_squad')
    players = models.ManyToManyField(Player, related_name='all_players')
    captain = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='captain')
    vice_captain = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='vice_captain')
    playing_eleven = models.ManyToManyField(Player, verbose_name='Playing XI', related_name='playing_eleven')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class Match(TimeStampedModel):
    STATUS = (
        ('Upcoming', 'Upcoming'),
        ('Live', 'Live'),
        ('Finished', 'Finished')
    )
    RESULT = (
        ('Completed', 'Completed'),
        ('Draw', 'Draw'),
        ('Abandoned', 'Abandoned')
    )
    TYPE = (
        ('T20', 'T20'),
        ('ODI', 'ODI'),
        ('Test', 'Test')
    )
    team_one = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_one')
    team_two = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_two')
    squad_one = models.ForeignKey(Squad, on_delete=models.CASCADE, related_name='squad_one')
    squad_two = models.ForeignKey(Squad, on_delete=models.CASCADE, related_name='squad_two')
    location = models.CharField(max_length=100)
    date = models.DateTimeField()
    toss = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True, related_name='toss')
    winner = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True, related_name='winner')
    status = models.CharField(max_length=10, choices=STATUS)
    result = models.CharField(max_length=10, choices=RESULT, null=True, blank=True)
    type = models.CharField(max_length=10, choices=TYPE)
    result_description = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name_plural = 'Matches'

    def __str__(self):
        return f"{self.team_one} VS {self.team_two}"
