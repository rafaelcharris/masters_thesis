from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import json

author = 'Felipe Montealegre'

doc = """
RAVEN
"""


class Constants(BaseConstants):
    name_in_url = 'Logica'
    players_per_group = None
    num_rounds = 1
    piece_rate = 1

    time_limit_raven = 60


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    is_correct_q1 = models.IntegerField()
    is_correct_q2 = models.IntegerField()
    is_correct_q3 = models.IntegerField()
    is_correct_q4 = models.IntegerField()
    is_correct_q5 = models.IntegerField()
    is_correct_q6 = models.IntegerField()
    is_correct_q7 = models.IntegerField()
    is_correct_q8 = models.IntegerField()
    is_correct_q9 = models.IntegerField()
    is_correct_q10 = models.IntegerField()

    accumulated_is_correct = models.IntegerField()

    piece_rate = models.IntegerField()
    accumulated_payoff = models.IntegerField()

    def variables(self):

        self.piece_rate = Constants.piece_rate

        is_correct_accumulated_list = [0 if e is None else e for e in [self.is_correct_q1, self.is_correct_q2, self.is_correct_q3, self.is_correct_q4, self.is_correct_q5, self.is_correct_q6, self.is_correct_q7, self.is_correct_q8, self.is_correct_q9, self.is_correct_q10]]
        piece_rate_list = [0 if e is None else e for e in [self.piece_rate, self.piece_rate, self.piece_rate, self.piece_rate, self.piece_rate, self.piece_rate, self.piece_rate, self.piece_rate, self.piece_rate, self.piece_rate]]

        self.accumulated_payoff = sum(i*j for i, j, in zip(is_correct_accumulated_list, piece_rate_list))
        self.accumulated_is_correct = sum(is_correct_accumulated_list)

        print("[[ RAVEN ]] - PLAYER - VARIABLES.............ROUND NUMBER:", self.round_number)
        print("[[ RAVEN ]] - PLAYER - VARIABLES .............IS_CORRECT_Q1:", self.is_correct_q1)
        print("[[ RAVEN ]] - PLAYER - VARIABLES .............IS_CORRECT_Q2:", self.is_correct_q2)
        print("[[ RAVEN ]] - PLAYER - VARIABLES .............IS_CORRECT_Q3:", self.is_correct_q3)
        print("[[ RAVEN ]] - PLAYER - VARIABLES .............IS_CORRECT_Q4:", self.is_correct_q4)
        print("[[ RAVEN ]] - PLAYER - VARIABLES .............IS_CORRECT_Q5:", self.is_correct_q5)
        print("[[ RAVEN ]] - PLAYER - VARIABLES .............IS_CORRECT_Q6:", self.is_correct_q6)
        print("[[ RAVEN ]] - PLAYER - VARIABLES .............IS_CORRECT_Q7:", self.is_correct_q7)
        print("[[ RAVEN ]] - PLAYER - VARIABLES .............IS_CORRECT_Q8:", self.is_correct_q8)
        print("[[ RAVEN ]] - PLAYER - VARIABLES .............IS_CORRECT_Q9:", self.is_correct_q9)
        print("[[ RAVEN ]] - PLAYER - VARIABLES .............IS_CORRECT_Q10:", self.is_correct_q10)
        print("[[ RAVEN ]] - PLAYER - VARIABLES .............IS_CORRECT_LIST:", [0 if e is None else e for e in [self.is_correct_q1, self.is_correct_q2, self.is_correct_q3, self.is_correct_q4, self.is_correct_q5, self.is_correct_q6, self.is_correct_q7, self.is_correct_q8, self.is_correct_q9, self.is_correct_q10]])
        print("[[ RAVEN ]] - PLAYER - VARIABLES .............PIECE_RATE:", [0 if e is None else e for e in [self.piece_rate, self.piece_rate, self.piece_rate, self.piece_rate, self.piece_rate, self.piece_rate, self.piece_rate, self.piece_rate, self.piece_rate, self.piece_rate]])
        print("[[ RAVEN ]] - PLAYER - VARIABLES .............ACCUMULATED_PAYOFF:", self.accumulated_payoff)
        print("[[ RAVEN ]] - END-----END-----END-----END-----END-----END-----END-----END-----END-----END-----END-----END-----END-----END-----END")

    def set_payoffs(self):
        self.payoff = self.accumulated_payoff

    def raven_admin(self):
        self.participant.vars['raven_total_is_correct'] = self.accumulated_is_correct
        self.participant.vars['raven_total_payoff'] = self.accumulated_payoff
        print("[[ RAVEN ]] - PLAYER - RAVEN_ADMIN.............ROUND NUMBER", self.round_number)
        print("[[ RAVEN ]] - PLAYER - RAVEN_ADMIN.............PVARS ARE", self.participant.vars)

