from django.contrib import admin

from .models import Club, Player, Team

admin.site.register(Club)
admin.site.register(Team)
admin.site.register(Player)
