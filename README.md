# Predicción de resultados de partidos de fútbol usando aprendizaje automático

Para desplegar la página web del proyecto, desde Visual Studio Code se deben realizar los siguientes pasos:

1.Situarse en la carpeta prediccion_partidos_futbol

2.Ejecutar los siguientes comandos:

    2.1. pip install numpy, pandas, sklearn==1.0.2, joblib, django, djangorestframework, django-crispy-forms
    2.2. python manage.py makemigrations
    2.3. python manage.py migrate
    2.4. python manage.py collectstatic
    2.5. python manage.py runserver

3.Acceder por navegador al la siguiente url: http://127.0.0.1:8000/