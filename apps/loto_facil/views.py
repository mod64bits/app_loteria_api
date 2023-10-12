from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import (
    BolaoSerializer, JogosSerializer, ConcursoSerializer, PremiosSerializer,
    ResultadoJogosSerializer
    )
from .models import Concurso, Jogos, Bolao, Premios
from apps.usuarios.serializers import ParticipantesSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated



class ConcursoViewSet(viewsets.ModelViewSet):
    queryset = Concurso.objects.all()
    serializer_class = ConcursoSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class JogosViewSet(viewsets.ModelViewSet):
    queryset = Jogos.objects.all()
    serializer_class = JogosSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class BolaoViewSet(viewsets.ModelViewSet):
    queryset = Bolao.objects.all()
    serializer_class = BolaoSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
    @action(detail=True, methods=['get'])
    def premios(self, request, pk=None):
        bolao = self.get_object()
        serialize = PremiosSerializer(bolao.premio_bolao.all(), many=True)
        return Response(serialize.data)
    
    @action(detail=True, methods=['get'])
    def resultados(self, request, pk=None):
        bolao = self.get_object()
        serialize = ResultadoJogosSerializer(bolao.result_bolao.all(), many=True)
        return Response(serialize.data)
    
    
    @action(methods=['post'], detail=True)
    def jogos(self, request, pk=None, *args, **kwargs):
        obj = self.get_object()
        serializer_jogos = JogosSerializer(data=request.data)
        if serializer_jogos.is_valid():
            jogo = serializer_jogos.save()
            obj.jogos = jogo
            obj.save()
            return Response({'status': 'Jogos adcionado ao bolao'})
        else:
            return Response(serializer_jogos.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    
class PremiosViewSet(viewsets.ModelViewSet):
    queryset = Premios.objects.all()
    serializer_class = PremiosSerializer

    # def get_queryset(self):
    #     return self.queryset.filter(bolao__id=self.kwargs.get('bolao_pk'))


