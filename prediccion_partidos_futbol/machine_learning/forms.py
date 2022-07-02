from django import forms
from .models import Match
from crispy_forms.helper import FormHelper

class MatchForm(forms.ModelForm):
    
    class Meta:
        model = Match
        fields = "__all__"

    liga = forms.TypedChoiceField(choices=[('ESP','España'),('IT','Italia'),('GER','Alemania'),('FR','Francia'),('ENG','Inglaterra')])
    año = forms.TypedChoiceField(choices=[(2015,2015),(2016,2016),(2017,2017),(2018,2018),(2019,2019),(2020,2020)])
    jornada = forms.IntegerField()
    equipo_local= forms.CharField(max_length=50)
    equipo_visitante= forms.CharField(max_length=50)
    