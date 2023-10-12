from rest_framework import serializers
from .models import Bolao, Jogos, Premios, Concurso, ResultadoJogos



class BolaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bolao
        fields = '__all__'


class JogosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogos
        fields = '__all__'


class PremiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Premios
        fields = '__all__'


class ConcursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concurso
        fields = '__all__'


class ResultadoJogosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultadoJogos
        fields = '__all__'