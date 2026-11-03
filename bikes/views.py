from django.shortcuts import render
from rest_framework import viewsets
from .models import Bike
from .serializer import BikeSerializer

class BikeViewSet(viewsets.ModelViewSet):
    queryset=Bike.objects.all()
    serializer_class=BikeSerializer

