from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        if self.player.round_number == 1:
            yield (pages.Sorteo)
            yield (pages.Question, {'sexo': 'Masculino', 'edad': 18, 'estado_civil': 'Soltera/o', 'carrera': 'Administración de Empresas', 'matricula': 8, 'ingreso': 3, 'localidad': 14, 'estrato': 4, 'edu_padre': 'Posgrado', 'edu_madre': 'Posgrado', 'peso': 68, 'altura': 178, 'fehr_1': 4, 'fehr_2': 4, 'seicientos': 'No tendría dificultad'})
        else:
            pass
