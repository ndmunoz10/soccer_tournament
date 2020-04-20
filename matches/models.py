from django.db import models


class Match(models.Model):
    home_team_name = models.CharField(max_length=300)
    home_team_score = models.IntegerField()
    away_team_name = models.CharField(max_length=300)
    away_team_score = models.IntegerField()
    stadium_name = models.CharField(max_length=300, default=None)
    date = models.CharField(max_length=10)
    start_time = models.CharField(max_length=10)

    def __str__(self):
        return self.home_team_name + " - " + self.away_team_name
