from django.contrib import admin

from .models import Competition, Draw, Game, Location, Result

admin.site.register(Location)
admin.site.register(Competition)
admin.site.register(Draw)
admin.site.register(Game)
admin.site.register(Result)
