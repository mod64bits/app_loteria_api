from django.db import models
from django_jsonform.models.fields import ArrayField
from django.conf import settings
from apps.core.models import Base
from apps.usuarios.models import Participantes
from django.db.models import signals



class Concurso(Base):
    concurso = models.CharField('Concurso', max_length=20, unique=True)
    data_sorteio = models.DateField('Data Sorteio')
    resultado = ArrayField(
        ArrayField(
            models.PositiveIntegerField(),
            size=15,
        ),
        size=1
    )

    def __str__(self):
        return self.concurso
    

class Jogos(Base):
    descricao = models.CharField('Descrição', max_length=50, unique=True)
    jogos = ArrayField(
        ArrayField(
            models.PositiveIntegerField(),

        ),

    )

    def __str__(self):
        return self.descricao
    
class Bolao(Base):
     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Usuário', null=True, blank=True)
     nome = models.CharField('Descrição', max_length=150, unique=True)
     participantes = models.ManyToManyField(Participantes, verbose_name='Participantes', related_name='bolao_participantes', null=True, blank=True)
     concursos = models.ManyToManyField(Concurso, verbose_name='Concurso', related_name='bolao_concursos', null=True, blank=True)
     jogos = models.ForeignKey(Jogos, on_delete=models.CASCADE, verbose_name='Jogos', related_name='jogos_bolao', null=True, blank=True)
     valor = models.DecimalField('Valor Jogos', decimal_places=2, max_digits=8, default=0)

     def __str__(self) -> str:
         return self.nome
     
    
class Premios(Base):
    concurso = models.ForeignKey(
        Concurso,
        verbose_name="Concuro",
        on_delete=models.CASCADE,
        related_name="premio_concurso"
        )
    bolao = models.ForeignKey(
        Bolao,
        on_delete=models.CASCADE,
        verbose_name='Bolão',
        related_name="premio_bolao"
    )

    valor = models.DecimalField('Valor Jogos', decimal_places=2, max_digits=8)
    quantidade_acertos = models.PositiveIntegerField('Quantidade de Acertos', default=11)


    def __str__(self) -> str:
        return f"{self.concurso}, {self.bolao}, {self.quantidade_acertos}" 
    

class ResultadoJogos(Base):
    concurso = models.ForeignKey(
        Concurso,
        on_delete=models.CASCADE,
        related_name='result_concurso',
        verbose_name='Concurso',
        null=True,
        blank=True
    )
    jogo = ArrayField(
        ArrayField(
            models.PositiveIntegerField(),
            size=15
        )
    )
    bolao = models.ForeignKey(
        Bolao,
        on_delete=models.CASCADE,
        related_name='result_bolao',
        verbose_name='Bolão',
        null=True,
        blank=True
    )
    acertos = ArrayField(
        ArrayField(
            models.PositiveIntegerField(),
        ),
        null=True, blank=True
    )
    qt_acertos = models.PositiveIntegerField('QUantidade Acertos', default=0)

    def __str__(self):
        return f"Concurso: {self.concurso.concurso} Bolão: {self.bolao.nome} Acertos: {self.qt_acertos}"
    





def total_acertos(jogo, concurso):
    acertos = [list(set(jogo) & set(concurso))]
    qt_acertos = len(acertos[0])
    return acertos, qt_acertos

def valor_premios(qt_acertos):
    if qt_acertos == 11:
        return 6.00
    elif qt_acertos == 12:
        return 12.00
    elif qt_acertos == 13:
        return 30.00
    elif qt_acertos == 14:
        return 1700.00
    elif qt_acertos == 15:
        return 1.00000
    else:
        return 0


def add_premios(sender, instance, signal, *args, **kwargs):
    _bolao = Bolao.objects.all()

    for item in _bolao:
        try:
            for i in item.jogos.jogos:
                acertos, qt_acertos = total_acertos(i, instance.resultado[0])
                if qt_acertos >10:
                    Premios.objects.create(
                        concurso=instance,
                        bolao=item,
                        valor=valor_premios(qt_acertos=qt_acertos),
                        quantidade_acertos=qt_acertos
                    )
                ResultadoJogos.objects.create(
                    concurso=instance,
                    jogo=[i],
                    bolao=item,
                    acertos=acertos,
                    qt_acertos=qt_acertos
                )
        except AttributeError:
            continue

        

                
              


signals.post_save.connect(add_premios, sender=Concurso)