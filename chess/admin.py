from django.contrib import admin

# Register your models here.
from .models import Player, Lobby

class ChessAdmin(admin.ModelAdmin):
    pass

admin.site.register(Player, ChessAdmin)
admin.site.register(Lobby, ChessAdmin)