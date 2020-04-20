from django.db import models


# Create your models here.

class Transfer(models.Model):
    name = models.CharField(max_length=100)
    old_team_name = models.CharField(max_length=100)
    new_team_name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.old_team_name + " - " + self.new_team_name
