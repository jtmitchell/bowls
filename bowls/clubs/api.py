# -*- coding: utf-8 -*-
from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer

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
