from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import LanguageSerializer, ParadigmSerializer, ProgrammerSerializer
from .models import language, Paradigm, Programmer
# Create your views here.

class LanguageView(viewsets.ModelViewSet):
    queryset = language.objects.all()
    serializer_class = LanguageSerializer
    
    #Autentica con permisos de administrador
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer

class ProgrammerView(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer
    permission_classes = [permissions.IsAuthenticated]