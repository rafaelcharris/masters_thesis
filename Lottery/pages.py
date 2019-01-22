from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Lottery(Page):

    form_model = 'player'
    form_fields = ['binary_lottery_1', 'binary_lottery_2', 'binary_lottery_3', 'binary_lottery_4', 'binary_lottery_5', 'binary_lottery_6']

    def before_next_page(self):
        #self.player.total_payoff()
        #self.player.lottery_admin()
        pass


class Results_lottery(Page):
    def vars_for_template(self):
        self.player.total_payoff()
        self.player.lottery_admin()
        self.player.set_payoffs()


page_sequence = [
    Lottery,
    Results_lottery
]
