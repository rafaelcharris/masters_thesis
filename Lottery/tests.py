from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        if self.player.round_number == 1:
            yield (pages.Lottery, {'binary_lottery_1': 1, 'binary_lottery_2': 1, 'binary_lottery_3': 1, 'binary_lottery_4': 1, 'binary_lottery_5': 1, 'binary_lottery_6': 1})
            yield (pages.Results_lottery)
        else:
            pass
