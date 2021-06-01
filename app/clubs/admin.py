# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Club, Team, Player

admin.site.register(Club)
admin.site.register(Team)
admin.site.register(Player)
