from .forms import MatchForm
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Match
from .serializer import MatchSerializers

import joblib
import pandas as pd
from django.shortcuts import render
import numpy as np


class MatchView(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializers


def status(df):
    try:
        model_espanya = joblib.load(
            'machine_learning\modelo_entrenado_españa.pkl')
        model_italia = joblib.load(
            'machine_learning\modelo_entrenado_italia.pkl')
        model_alemania = joblib.load(
            'machine_learning\modelo_entrenado_alemania.pkl')
        model_francia = joblib.load(
            'machine_learning\modelo_entrenado_francia.pkl')
        model_inglaterra = joblib.load(
            'machine_learning\modelo_entrenado_inglaterra.pkl')

        if df['País'].values[0] == 'ESP':
            y_pred = model_espanya.predict_proba(
                df.drop(columns=["Resultado"]))
            y_pred = y_pred[-1]
        elif df['País'].values[0] == 'IT':
            y_pred = model_italia.predict_proba(df.drop(columns=["Resultado"]))
            y_pred = y_pred[-1]
        elif df['País'].values[0] == 'GER':
            y_pred = model_alemania.predict_proba(
                df.drop(columns=["Resultado"]))
            y_pred = y_pred[-1]
        elif df['País'].values[0] == 'FR':
            y_pred = model_francia.predict_proba(
                df.drop(columns=["Resultado"]))
            y_pred = y_pred[-1]
        else:
            y_pred = model_inglaterra.predict_proba(
                df.drop(columns=["Resultado"]))
            y_pred = y_pred[-1]

        prob_local = str(round(y_pred[0], 4) * 100)[0:5] + "%"
        prob_empate = str(round(y_pred[1], 4) * 100)[0:5] + "%"
        prob_visitante = str(round(y_pred[2], 4) * 100)[0:5] + "%"

        mayor_prob=np.where(y_pred == max(y_pred))

        equipo_local=df.iloc[len(df)-1]["Equipo local"]
        equipo_visitante=df.iloc[len(df)-1]["Equipo visitante"]

        if mayor_prob[0][0] == 0:
            resultado = "Victoria para " + \
                df.iloc[len(df)-1]["Equipo local"]
        elif mayor_prob[0][0] ==1:
            resultado = " Empate"
        else:
            resultado = "Victoria para " + \
                df.iloc[len(df)-1]["Equipo visitante"]

        result = {'local': prob_local, 'empate': prob_empate,'visitante': prob_visitante,'resultado':resultado,'equipo_local':equipo_local,'equipo_visitante':equipo_visitante}

        return result
        

    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


def FormView(request):
    if request.method == 'POST':
        form = MatchForm(request.POST or None)

        if form.is_valid():
            league = form.cleaned_data['liga']
            year = form.cleaned_data['año']
            matchday = form.cleaned_data['jornada']
            local_team = form.cleaned_data['equipo_local']
            away_team = form.cleaned_data['equipo_visitante']

            if league == 'ESP':
                df = pd.read_csv("machine_learning/bbdd_esp.csv",
                                 sep=",", encoding='utf-8', index_col=0)
            elif league == 'IT':
                df = pd.read_csv("machine_learning/bbdd_it.csv",
                                 sep=",", encoding='utf-8', index_col=0)
            elif league == 'GER':
                df = pd.read_csv("machine_learning/bbdd_ale.csv",
                                 sep=",", encoding='utf-8', index_col=0)
            elif league == 'FR':
                df = pd.read_csv("machine_learning/bbdd_fr.csv",
                                 sep=",", encoding='utf-8', index_col=0)
            else:
                df = pd.read_csv("machine_learning/bbdd_en.csv",
                                 sep=",", encoding='utf-8', index_col=0)

            df = df.append({'Año': year, 'País': league, 'Jornada': matchday,
                           'Equipo local': local_team, 'Equipo visitante': away_team}, ignore_index=True)

            result = status(df)
            return render(request, 'status.html', {"data": result})

    form = MatchForm()

    return render(request, 'form.html', {'form': form})
