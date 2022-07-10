# Predicción de resultados de partidos de fútbol usando aprendizaje automático

Para desplegar la página web del proyecto, desde Visual Studio Code se deben realizar los siguientes pasos:

1.Abrir un nuevo terminal

2.Ejecutar el comando: 
    * git clone https://github.com/rodrigoec11/Prediccion-de-resultados-de-partidos-de-futbol-usando-aprendizaje-automatico.git

3.Situarse en la carpeta prediccion_partidos_futbol con el siguiente comando: 
    * cd Prediccion-de-resultados-de-partidos-de-futbol-usando-aprendizaje-automatico/prediccion_partidos_futbol

4. Ejecutar los siguientes comandos por orden:

    * pip install numpy, pandas, sklearn, joblib, django, djangorestframework, django-crispy-forms
    * python manage.py makemigrations
    * python manage.py migrate
    * python manage.py collectstatic
    * python manage.py runserver

5.Acceder por navegador al la siguiente url: http://127.0.0.1:8000/
