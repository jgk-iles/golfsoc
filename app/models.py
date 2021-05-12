from django.db import models
from django.db.models import indexes
from django.db.models.aggregates import Max
from django.db.models.lookups import IsNull


class Course(models.Model):
    name = models.CharField(max_length=50)
    par = models.IntegerField()
    yardage = models.IntegerField()
    slope = models.FloatField()

    def __str__(self) -> str:
        return self.name


class Hole(models.Model):
    hole_number = models.IntegerField()
    course = models.ForeignKey("Course", on_delete=models.CASCADE)
    par = models.IntegerField()
    yardage = models.IntegerField()

    def __str__(self) -> str:
        return f"Hole {self.hole_number} of {self.course}"


class PlayerScorecard(models.Model):
    played_by = models.ForeignKey("Player", on_delete=models.CASCADE)
    part_of_round = models.ForeignKey("Round", on_delete=models.CASCADE)

    # Gross scores
    hole1_gross = models.IntegerField(null=True, blank=True)
    hole2_gross = models.IntegerField(null=True, blank=True)
    hole3_gross = models.IntegerField(null=True, blank=True)
    hole4_gross = models.IntegerField(null=True, blank=True)
    hole5_gross = models.IntegerField(null=True, blank=True)
    hole6_gross = models.IntegerField(null=True, blank=True)
    hole7_gross = models.IntegerField(null=True, blank=True)
    hole8_gross = models.IntegerField(null=True, blank=True)
    hole9_gross = models.IntegerField(null=True, blank=True)
    hole10_gross = models.IntegerField(null=True, blank=True)
    hole11_gross = models.IntegerField(null=True, blank=True)
    hole12_gross = models.IntegerField(null=True, blank=True)
    hole13_gross = models.IntegerField(null=True, blank=True)
    hole14_gross = models.IntegerField(null=True, blank=True)
    hole15_gross = models.IntegerField(null=True, blank=True)
    hole16_gross = models.IntegerField(null=True, blank=True)
    hole17_gross = models.IntegerField(null=True, blank=True)
    hole18_gross = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return f"Scorecard of {self.played_by} for {self.part_of_round}"


class Round(models.Model):
    GAME_CHOICES = (
        ('Stroke Play', 'stroke play'),
        ('Stableford', 'stableford'),
        ('Four Balls', 'four balls'),
    )
    date_played = models.DateField(auto_now_add=True)
    course = models.ForeignKey("Course", on_delete=models.SET("Blank"))
    society = models.ForeignKey(
        "Society", blank=True, null=True, on_delete=models.SET_NULL)
    game_type = models.CharField(max_length=15, choices=GAME_CHOICES)

    def __str__(self) -> str:
        if self.society:
            return f"{self.game_type} round at {self.course} played on {self.date_played}"
        else:
            return f"{self.game_type} at {self.course} played on {self.date_played}"


class Player(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # rounds_played = models.ManyToManyField("PlayerScorecard", blank=True)
    # handicap = models.OneToOneField(
    #     "handicap", null=True, blank=True, on_delete=models.SET_NULL)
    handicap = models.FloatField(default=28.0)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


# class Handicap(models.Model):
#     handicap_index = models.FloatField()
#     latest_update = models.DateField(auto_now=True)

#     def __str__(self) -> str:
#         return f"{self.player}'s Handicap: {self.handicap}"


class Society(models.Model):
    name = models.CharField(max_length=50, unique=True)
    date_founded = models.DateField(auto_now_add=True)
    players = models.ManyToManyField(Player, blank=True)

    class Meta:
        verbose_name_plural = "Societies"

    def __str__(self):
        return self.name
