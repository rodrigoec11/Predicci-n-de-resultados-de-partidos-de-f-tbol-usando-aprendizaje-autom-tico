from rest_framework import serializers 
from .models import Match 

class MatchSerializers(serializers.ModelSerializer): 
    class meta: 
        model=Match 
        fields='__all__'