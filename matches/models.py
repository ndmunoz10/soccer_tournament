from django.db import models


class Goal(models.Model):
    player_name = models.CharField(max_length=100)
    minute = models.IntegerField()
    team = models.CharField(max_length=100)
    pass

    def __str__(self):
        return self.player_name


class FreeKick(models.Model):
    shooter_name = models.CharField(max_length=100)
    barrier_names = models.CharField(max_length=300)
    team_name = models.CharField(max_length=100)

    def __str__(self):
        return self.shooter_name


class Fault(models.Model):
    reason = models.CharField(max_length=300)
    minute = models.IntegerField()
    team_name = models.CharField(max_length=100)
    card = models.CharField(max_length=32)
    pass

    def __str__(self):
        return self.team_name + " - " + self.reason


class Change(models.Model):
    in_player_name = models.CharField(max_length=100)
    out_player_name = models.CharField(max_length=100)
    minute = models.IntegerField()
    team_name = models.CharField(max_length=100)
    pass

    def __str__(self):
        return self.team_name


class Match(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    free_kick = models.ForeignKey(FreeKick, on_delete=models.CASCADE)
    fault = models.ForeignKey(Fault, on_delete=models.CASCADE)
    change = models.ForeignKey(Change, on_delete=models.CASCADE)
    home_team_name = models.CharField(max_length=300)
    home_team_score = models.IntegerField()
    away_team_name = models.CharField(max_length=300)
    away_team_score = models.IntegerField()
    stadium_name = models.CharField(max_length=300, default=None)
    date = models.CharField(max_length=10)
    start_time = models.CharField(max_length=10)

    def __str__(self):
        return self.home_team_name + " - " + self.away_team_name

