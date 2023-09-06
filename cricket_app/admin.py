from django.contrib import admin

from cricket_app.models import Team, Player, Squad, Match

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Squad)
admin.site.register(Match)
