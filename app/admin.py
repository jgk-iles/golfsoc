from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Player, Course, Hole, Society, PlayerScorecard, Round


# admin.site.register(Player)
admin.site.register(Course)
admin.site.register(Hole)
admin.site.register(Society)
# admin.site.register(Handicap)
admin.site.register(PlayerScorecard)
# admin.site.register(Round)


class PlayerScorecardsInline(admin.StackedInline):
    model = PlayerScorecard
    extra = 0


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    inlines = [
        PlayerScorecardsInline,
    ]


@admin.register(Round)
class RoundAdmin(admin.ModelAdmin):
    inlines = [
        PlayerScorecardsInline,
    ]
