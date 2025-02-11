from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet   
from .models import estado, cidade, pessoa
from .serializers import estadoSerializer, cidadeSerializer, pessoaSerializer

# Create your views here.

class estadoViewSet(ModelViewSet):
    queryset = estado.objects.all()
    serializer_class = estadoSerializer

class cidadeViewSet(ModelViewSet):
    queryset = cidade.objects.all()
    serializer_class = cidadeSerializer

class pessoaViewSet(ModelViewSet):
    queryset = pessoa.objects.all()
    serializer_class = pessoaSerializer
