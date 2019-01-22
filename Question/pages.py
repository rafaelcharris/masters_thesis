from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class NormalWaitPage(WaitPage):
    body_text = "Por favor espere a los otros participantes para dar inicio al sorteo de la actividad a pagar de la " \
                "segunda parte del ejercicio"


class Sorteo(Page):
    def vars_for_template(self):
        return {
            'sumas_total_payoff': self.player.participant.vars.get('sumas_total_payoff'),
            'memory_total_payoff': self.player.participant.vars.get('memory_total_payoff'),
            'dados_total_payoff': self.player.participant.vars.get('dados_payoff'),
            'lottery_total_payoff': self.player.participant.vars.get('lottery_total_payoff'),
            'raven_total_payoff': self.player.participant.vars.get('raven_total_payoff'),
        }


class Question(Page):
    pass

    form_model = 'player'
    form_fields = ['sexo', 'edad', 'estado_civil', 'carrera', 'matricula', 'ingreso', 'localidad', 'estrato', 'edu_padre', 'edu_madre', 'peso', 'altura', 'fehr_1', 'fehr_2', 'seicientos']

    #def before_next_page(self):
    #    self.player.consent_admin()


page_sequence = [
    NormalWaitPage,
    Sorteo,
    Question,
]
