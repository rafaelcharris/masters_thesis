from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):

        yield (pages.Intro_raven)
        yield (pages.Q1, {'is_correct_q1': 1})
        yield (pages.Q2, {'is_correct_q2': 1})
        yield (pages.Q3, {'is_correct_q3': 1})
        yield (pages.Q4, {'is_correct_q4': 1})
        yield (pages.Q5, {'is_correct_q5': 1})
        yield (pages.Q6, {'is_correct_q6': 1})
        yield (pages.Q7, {'is_correct_q7': 1})
        yield (pages.Q8, {'is_correct_q8': 1})
        yield (pages.Q9, {'is_correct_q9': 1})
        yield (pages.Q10, {'is_correct_q10': 1})
        yield (pages.Results_raven)
