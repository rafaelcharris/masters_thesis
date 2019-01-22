from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import time


class Intro_sumas(Page):

    def is_displayed(self):
        return self.player.round_number == 1

    # http://otree.readthedocs.io/en/latest/timeouts.html
    def before_next_page(self):
        self.participant.vars['expiry'] = time.time() + Constants.time_limit
        #self.subsession.tratamientos()


class Sumas(Page):

    form_model = 'player'
    form_fields = ['respuesta']

    # http://otree.readthedocs.io/en/latest/timeouts.html
    def get_timeout_seconds(self):
        if self.player.round_number <= 50:
            return self.participant.vars['expiry'] - time.time()
        elif self.player.round_number > 50 and self.player.round_number <= 100:
            return self.participant.vars['expiry'] - time.time()


    def is_displayed(self):
        if self.player.round_number <= 50:
            return self.participant.vars['expiry'] - time.time() > 0
        elif self.player.round_number > 50 and self.player.round_number <= 100:
            return self.participant.vars['expiry'] - time.time() > 0


    def before_next_page(self):
        self.player.variables_totales()

    def vars_for_template(self):

        #self.player.tratamientos()
        self.player.variables_acumuladas()
        #self.player.set_payoffs()

        # mensaje de si la ronda anterior fue correcta o no
        if self.player.round_number == 1:  # on very first task
            correct_last_round = ""
        else:  # all subsequent tasks
            if self.player.in_previous_rounds()[-1].is_correct:
                correct_last_round = "correcta"
            else:
                correct_last_round = "incorrecta"
        return (
            {
                'round_count': (self.player.round_number - 1),
                'correct_last_round': correct_last_round,
                'accumulated_is_correct': self.player.accumulated_is_correct,
                'accumulated_payoff': self.player.accumulated_payoff,
                'piece_rate': self.player.piece_rate
            }
        )


class Anuncio(Page):

    def is_displayed(self):
        return self.player.round_number == Constants.half_way

    # http://otree.readthedocs.io/en/latest/timeouts.html
    def before_next_page(self):
        self.participant.vars['expiry'] = time.time() + Constants.time_limit

    def vars_for_template(self):
        self.player.variables_totales()
        return {'accumulated_before': self.player.total_payoff,
                'accumulated_after': int(self.player.total_payoff / 2)}


class Results_sumas(Page):

    timeout_seconds = 30

    def is_displayed(self):
        return self.player.round_number == Constants.num_rounds

    def vars_for_template(self):

        self.player.variables_totales()
        self.player.variables_acumuladas()
        self.player.set_payoffs()
        self.player.sumas_admin()
        # mensaje con tabla resumen en la pagina Results
        table_rows = []
        for prev_player in self.player.in_all_rounds():
            if prev_player.respuesta is not None:
                if prev_player.respuesta > 0:
                    row = {
                        'num_ronda': prev_player.round_number,
                        'sumando_1': prev_player.sumando_1,
                        'sumando_2': prev_player.sumando_2,
                        'sumando_3': prev_player.sumando_3,
                        'sumando_4': prev_player.sumando_4,
                        'sumando_5': prev_player.sumando_5,
                        'solucion': prev_player.solucion,
                        'respuesta': prev_player.respuesta,
                        'is_correct': prev_player.is_correct,
                        'treatment': prev_player.treatment,
                        'piece_rate': prev_player.piece_rate,
                        'total_payoff': prev_player.total_payoff,
                    }
                    table_rows.append(row)
        return {'table_rows': table_rows}


page_sequence = [
    Intro_sumas,
    Sumas,
    Anuncio,
    Results_sumas]
