from pyexpat import model
from attr import field, fields
from rest_framework import serializers
from .models import users

class usersSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = users
        fields = ('userid','firstname','lastname','emailid','salry')
        
        fields = '__all__'