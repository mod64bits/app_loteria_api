from django.contrib import admin
from .models import Bolao, Concurso, Jogos, Premios, ResultadoJogos
from apps.usuarios.models import Participantes

admin.site.register(Bolao)
admin.site.register(ResultadoJogos)
admin.site.register(Concurso)
admin.site.register(Jogos)
admin.site.register(Premios)
admin.site.register(Participantes)
