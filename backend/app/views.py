from django.shortcuts import render

from .models import Modelone
from .serializers import ModeloneSerializer
from rest_framework import generics

# Create your views here.



class ModeloneListCreate(generics.ListCreateAPIView):
    queryset = Modelone.objects.all()
    serializer_class = ModeloneSerializer
    


