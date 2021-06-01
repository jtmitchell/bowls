from django.db import models

from clubs.models import Team


class Location(models.Model):
    '''Place where the games are played.
    May be a stadium venue, or a single green for bowls.
    '''
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __unicode__(self):
        return self.name


class Competition(models.Model):
    name = models.CharField(max_length=255, blank=True, default='')
    teams = models.ManyToManyField(Team)

    def __unicode__(self):
        return self.name


class Draw(models.Model):
    '''A series of games within a competition.'''
    TYPE_ROUND_ROBIN = 'roundrobin'
    TYPE_KNOCKOUT = 'knockout'
    TYPE_CHOICES = (
            (TYPE_ROUND_ROBIN, 'Round Robin'),
            (TYPE_KNOCKOUT, 'Knockout Round'),
        )
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, default='')
    teams = models.ManyToManyField(Team)
    draw_type = models.CharField(max_length=20,
        db_index=True,
        choices=TYPE_CHOICES,
        default=TYPE_ROUND_ROBIN,
        )
    draw_order = models.IntegerField(default=1)

    def __unicode__(self):
        return '%s %s' % (self.competition, self.name)


class Game(models.Model):
    '''A single game between teams.
    Usually 2 teams.
    The game is at a location,
    and the start/end times define the location booking.
    '''
    draw = models.ForeignKey(Draw, on_delete=models.CASCADE)
    teams = models.ManyToManyField(Team)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __unicode__(self):
        return '%s in %s' % (' vs '.join(
            [x.name for x in self.teams], self.draw
            ))


class Result(models.Model):
    '''The result of a game, for a single team.
    '''
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __unicode__(self):
        return '%s %s (%s)' % (self.team, self.score, self.game)
