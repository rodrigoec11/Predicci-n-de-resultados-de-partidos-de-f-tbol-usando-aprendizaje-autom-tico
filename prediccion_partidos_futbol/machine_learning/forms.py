from django import forms
from .models import Match
from crispy_forms.helper import FormHelper
from django.core.exceptions import ValidationError


class MatchForm(forms.ModelForm):

    class Meta:
        model = Match
        fields = "__all__"

    liga = forms.TypedChoiceField(choices=[('ESP', 'España'), ('IT', 'Italia'), (
        'GER', 'Alemania'), ('FR', 'Francia'), ('ENG', 'Inglaterra')])
    año = forms.IntegerField(
        help_text="Introduce un número entre 2015 y 2022.")
    jornada = forms.IntegerField(
        help_text="Introduce un número entre 1 y 34 (liga alemana) o entre 1 y 38 (resto de ligas).")
    equipo_local = forms.CharField(max_length=50)
    equipo_visitante = forms.CharField(max_length=50)

    def clean_año(self):
        data = self.cleaned_data['año']

        if data < 2015 or data > 2022:
            raise ValidationError(('El año introducido no es correcto'))

        return data

    def clean_jornada(self):
        data = self.cleaned_data['jornada']
        liga = self.cleaned_data['liga']

        if liga == 'GER' and data > 34 and data > 0:
            raise ValidationError(('La jornada introducida no es correcta'))
        elif data > 0 and data > 38:
            raise ValidationError(('La jornada introducida no es correcta'))

        return data
