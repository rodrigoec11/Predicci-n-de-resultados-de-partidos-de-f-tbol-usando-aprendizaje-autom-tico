from .forms import MatchForm
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Match
from .serializer import MatchSerializers

import joblib
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages


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
            y_pred = model_espanya.predict(df)
        elif df['País'].values[0] == 'IT':
            y_pred = model_italia.predict(df)
        elif df['País'].values[0] == 'GER':
            y_pred = model_alemania.predict(df)
        elif df['País'].values[0] == 'FR':
            y_pred = model_francia.predict(df)
        else:
            y_pred = model_inglaterra.predict(df)
        
        if y_pred[len(y_pred)-1] == 0:
            result = "Victoria para " + \
                df.iloc[len(df)-1]["Equipo local"]
        elif y_pred[len(y_pred)-1] == 1:
            result = " Empate"
        else:
            result = "Victoria para " + \
                df.iloc[len(df)-1]["Equipo visitante"]
        

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
                df = pd.read_csv("machine_learning/bbdd_esp.csv", sep=",", encoding='utf-8', index_col=0)
            elif league == 'IT':
                df = pd.read_csv("machine_learning/bbdd_it.csv",sep=",", encoding='utf-8', index_col=0)
            elif league == 'GER':
                df = pd.read_csv("machine_learning/bbdd_ale.csv",sep=",", encoding='utf-8', index_col=0)
            elif league == 'FR':
                df = pd.read_csv("machine_learning/bbdd_fr.csv",sep=",", encoding='utf-8', index_col=0)
            else:
                df = pd.read_csv("machine_learning/bbdd_en.csv",sep=",", encoding='utf-8', index_col=0)

            df = df.append({'Año': year, 'País':league, 'Jornada': matchday, 'Equipo local': local_team, 'Equipo visitante': away_team }, ignore_index=True)

            result = status(df)
            return render(request, 'status.html', {"data": result})

    form = MatchForm()

    return render(request, 'form.html', {'form': form})
