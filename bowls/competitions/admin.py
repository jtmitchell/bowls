# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Location, Competition, Draw, Game, Result

admin.site.register(Location)
admin.site.register(Competition)
admin.site.register(Draw)
admin.site.register(Game)
admin.site.register(Result)
