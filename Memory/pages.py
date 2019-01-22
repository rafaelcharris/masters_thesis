from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import time


class Intro_memory(Page):

    def is_displayed(self):
        return self.player.round_number == 1

    # http://otree.readthedocs.io/en/latest/timeouts.html
    def before_next_page(self):
        self.participant.vars['expiry_set20'] = time.time() + Constants.time_limit_set20

class Set_20(Page):

    def is_displayed(self):
        if (self.player.round_number == 1) and (self.participant.vars['expiry_set20'] - time.time() > 0):
            return True
        else:
            return False

    # http://otree.readthedocs.io/en/latest/timeouts.html
    def get_timeout_seconds(self):
        return self.participant.vars['expiry_set20'] - time.time()

 #   def is_displayed(self):
 #       return self.participant.vars['expiry_set20'] - time.time() > 0

    def before_next_page(self):
        self.participant.vars['expiry_set3'] = time.time() + Constants.time_limit_set3


class Set_3(Page):

    form_model = 'player'
    form_fields = ['is_correct']

    def vars_for_template(self):
        return {
            'image_id_1': 'set_3_{}_1'.format(self.player.round_number),
            'image_id_2': 'set_3_{}_2'.format(self.player.round_number),
            'image_id_3': 'set_3_{}_3'.format(self.player.round_number),
        }

    # http://otree.readthedocs.io/en/latest/timeouts.html
    def get_timeout_seconds(self):
        return self.participant.vars['expiry_set3'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_set3'] - time.time() > 0

    def before_next_page(self):
        self.player.variables_acumuladas()


class Results_memory(Page):

    def is_displayed(self):
        return self.player.round_number == Constants.num_rounds

    def vars_for_template(self):
        self.player.variables_acumuladas()
        self.player.set_payoffs()
        self.player.memory_admin()


page_sequence = [
    Intro_memory,
    Set_20,
    Set_3,
    Results_memory,
]
