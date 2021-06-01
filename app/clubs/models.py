from django.db import models


class Club(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    contact = models.CharField(max_length=255, blank=True, default='')

    def __unicode__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Player(models.Model):
    given_name = models.CharField(max_length=255, db_index=True)
    family_name = models.CharField(max_length=255, db_index=True)
    club = models.ForeignKey(Club, blank=True, null=True, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __unicode__(self):
        return '%s, %s' % (self.family_name, self.given_name)
