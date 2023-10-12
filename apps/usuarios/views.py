from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Participantes
from .serializers import ParticipantesSerializer


class ParticipantesViewSet(viewsets.ModelViewSet):
    queryset = Participantes.objects.all()
    serializer_class = ParticipantesSerializer
