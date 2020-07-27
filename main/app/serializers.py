from rest_framework import serializers
from .models import Modelone

class ModeloneSerializer(serializers.Serializer):
    class Meta:
        model = Modelone
        fields = ('id', 'name', 'email', 'message')
        
    def create(self,validated_data):
           return self.Meta.model.objects.create(**validated_data)
        
