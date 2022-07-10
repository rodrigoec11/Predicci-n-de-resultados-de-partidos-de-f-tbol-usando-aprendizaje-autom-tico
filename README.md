# Predicción de resultados de partidos de fútbol usando aprendizaje automático

Para desplegar la página web del proyecto, desde Visual Studio Code se deben realizar los siguientes pasos:

1. Situarse en la carpeta prediccion_partidos_futbol

2. Ejecutar los siguientes comandos:

    pip install numpy, pandas, sklearn==1.0.2, joblib, django, djangorestframework, django-crispy-forms
    python manage.py makemigrations
    python manage.py migrate
    python manage.py collectstatic
    python manage.py runserver

3.Acceder por navegador al la siguiente url: http://127.0.0.1:8000/
