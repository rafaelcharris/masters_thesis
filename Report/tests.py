from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
from otree.api import Submission


class PlayerBot(Bot):

    def play_round(self):
        yield Submission(pages.Fin, {'e_mail': 'afmontealegreol@unal.edu.co'}, check_html=False)
