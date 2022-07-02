from django.db import models

class Match(models.Model ):
    LEAGUE_CHOICES = (('ESP','España'),('IT','Italia'),('GER','Alemania'),('FR','Francia'),('ENG','Inglaterra'))
    YEAR_CHOICES = ((2015,2015),(2016,2016),(2017,2017),(2018,2018),(2019,2019),(2020,2020))

    liga = models.CharField(max_length=10, choices=LEAGUE_CHOICES)
    año = models.IntegerField(choices=YEAR_CHOICES)
    jornada = models.IntegerField()
    equipo_local= models.CharField(max_length=50)
    equipo_visitante= models.CharField(max_length=50)

