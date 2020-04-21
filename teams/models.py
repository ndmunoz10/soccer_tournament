from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)
    population_size = models.IntegerField()
    pass

    def __str__(self):
        return self.name


class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    legal_representative = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    origin_city = models.CharField(max_length=100)
    pass

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    creation_year = models.IntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
