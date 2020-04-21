from django.db import models


class Stadium(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=100)
    opening_year = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return self.name
