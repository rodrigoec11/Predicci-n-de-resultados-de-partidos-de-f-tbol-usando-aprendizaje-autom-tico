from django.db import models

class Match(models.Model):
    LEAGUE_CHOICES = (('ESP','España'),('IT','Italia'),('GER','Alemania'),('FR','Francia'),('ENG','Inglaterra'))

    liga = models.CharField(max_length=10, choices=LEAGUE_CHOICES)
    año = models.IntegerField()
    jornada = models.IntegerField()
    equipo_local= models.CharField(max_length=50)
    equipo_visitante= models.CharField(max_length=50)

