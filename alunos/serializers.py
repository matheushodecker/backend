from rest_framework.serializers import ModelSerializer
from .models import estado, cidade, pessoa

class estadoSerializer(ModelSerializer):
    class Meta:
        model = estado
        fields = '__all__'

class cidadeSerializer(ModelSerializer):
    class Meta:
        model = cidade
        fields = '__all__'

class pessoaSerializer(ModelSerializer):
    class Meta:
        model = pessoa
        fields = '__all__'