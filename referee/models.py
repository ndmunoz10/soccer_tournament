from django.db import models


class Referee(models.Model):
    id_card = models.IntegerField()
    name = models.CharField(max_length=100)
    tutor = models.CharField(max_length=100)

    def __str__(self):
        return self.name
