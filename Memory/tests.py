from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
from otree.api import Submission


class PlayerBot(Bot):

    def play_round(self):
        if self.player.round_number == 1:
            yield (pages.Intro_memory)
            yield Submission(pages.Set_20, check_html=False)
            yield (pages.Set_3, {'is_correct': 1})
        elif self.player.round_number == 2:
            yield (pages.Set_3, {'is_correct': 1})
        elif self.player.round_number == 3:
            yield (pages.Set_3, {'is_correct': 1})
        elif self.player.round_number == 4:
            yield (pages.Set_3, {'is_correct': 1})
        elif self.player.round_number == 5:
            yield (pages.Set_3, {'is_correct': 1})
        elif self.player.round_number == 6:
            yield (pages.Set_3, {'is_correct': 1})
        elif self.player.round_number == 7:
            yield (pages.Set_3, {'is_correct': 1})
        elif self.player.round_number == 8:
            yield (pages.Set_3, {'is_correct': 1})
        elif self.player.round_number == 9:
            yield (pages.Set_3, {'is_correct': 1})
        elif self.player.round_number == 10:
            yield (pages.Set_3, {'is_correct': 1})
        elif self.player.round_number == 11:
            yield (pages.Set_3, {'is_correct': 1})
        elif self.player.round_number == 12:
            yield (pages.Set_3, {'is_correct': 1})
        elif self.player.round_number == 13:
            yield (pages.Set_3, {'is_correct': 1})
        elif self.player.round_number == 14:
            yield (pages.Set_3, {'is_correct': 1})
        elif self.player.round_number == 15:
            yield (pages.Set_3, {'is_correct': 1})
        elif self.player.round_number == 16:
            yield (pages.Set_3, {'is_correct': 1})
        elif self.player.round_number == 17:
            yield (pages.Set_3, {'is_correct': 1})
        elif self.player.round_number == 18:
            yield (pages.Set_3, {'is_correct': 1})
        elif self.player.round_number == 19:
            yield (pages.Set_3, {'is_correct': 1})
        elif self.player.round_number == 20:
            yield (pages.Set_3, {'is_correct': 1})
            yield (pages.Results_memory)
        else:
            pass
