# -*- coding: utf-8 -*-
from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer

from clubs.models import Team, Player

from .models import Club


class ClubResource(DjangoResource):
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'name': 'name',
        'address': 'address',
        'contact': 'contact',
    })

    """
    @api {get} /api/clubs/ Request a list of Clubs
    @apiName ListClubs
    @apiGroup Club

    @apiSuccess {Object[]} clubs List of clubs
    """
    def list(self):
        return Club.objects.all()

    """
    @api {get} /api/clubs/:id Request club information
    @apiName GetClub
    @apiGroup Club

    @apiParam {Number} id Club unique id

    @apiSuccess {String} name Club name
    @apiSuccess {String} address Club address
    @apiSuccess {String} contact Club contact details
    """
    def detail(self, pk):
        return Club.objects.get(pk=pk)


class TeamResource(DjangoResource):
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'name': 'name',
    })

    """
    @api {get} /api/teams/ Request a list of Teams
    @apiName ListTeams
    @apiGroup Team

    @apiSuccess {Object[]} teams List of teams
    """
    def list(self):
        return Team.objects.all()

    """
    @api {get} /api/teams/:id Request team information
    @apiName GetTeam
    @apiGroup Team

    @apiParam {Number} id Team unique id

    @apiSuccess {String} name Team name
    """
    def detail(self, pk):
        return Team.objects.get(pk=pk)


class PlayerResource(DjangoResource):
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'name': 'name',
    })

    """
    @api {get} /api/players/ Request a list of Players
    @apiName ListPlayers
    @apiGroup Player

    @apiSuccess {Object[]} players List of Players
    """
    def list(self):
        return Player.objects.all()

    """
    @api {get} /api/players/:id Request Player information
    @apiName GetPlayer
    @apiGroup Player

    @apiParam {Number} id Player unique id

    @apiSuccess {String} name Player name
    """
    def detail(self, pk):
        return Player.objects.get(pk=pk)
