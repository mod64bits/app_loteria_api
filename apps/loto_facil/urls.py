from django.urls import path
from .views import BolaoViewSet, JogosViewSet, PremiosViewSet, ConcursoViewSet
from rest_framework import routers
from django.urls import path, include
from apps.usuarios.views import ParticipantesViewSet

router = routers.SimpleRouter()

router.register(r'bolao', BolaoViewSet)
router.register(r'jogos', JogosViewSet)
router.register(r'premios', PremiosViewSet)
router.register(r'concursos', ConcursoViewSet)
router.register(r'participantes', ParticipantesViewSet)



urlpatterns = [
    path('', include((router.urls, 'lotofacil'))),
]