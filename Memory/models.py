from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import json

author = 'Felipe Montealegre'

doc = """
MEMORY
"""


class Constants(BaseConstants):
    name_in_url = 'Memoria'
    players_per_group = None
    num_rounds = 20
    piece_rate = 1

    time_limit_set20 = 30
    time_limit_set3 = 60


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    is_correct = models.IntegerField()
    accumulated_is_correct = models.IntegerField()
    piece_rate = models.IntegerField()
    accumulated_payoff = models.IntegerField()

    def variables_acumuladas(self):
        is_correct_accumulated_list = [0 if e is None else e for e in [p.is_correct for p in self.in_rounds(1, Constants.num_rounds)]]
        self.accumulated_is_correct = sum(is_correct_accumulated_list)

        self.piece_rate = Constants.piece_rate
        piece_rate_list = [0 if e is None else e for e in [p.piece_rate for p in self.in_rounds(1, Constants.num_rounds)]]
        self.accumulated_payoff = sum(i*j for i, j, in zip(is_correct_accumulated_list, piece_rate_list))

        print("[[ MEMORY ]] - PLAYER - VARIABLES ACUMULADAS.............ROUND NUMBER:", self.round_number)
        print("[[ MEMORY ]] - PLAYER - VARIABLES ACUMULADAS.............IS_CORRECT:", self.is_correct)
        print("[[ MEMORY ]] - PLAYER - VARIABLES ACUMULADAS.............IS_CORRECT_LIST:", [0 if e is None else e for e in [p.is_correct for p in self.in_rounds(1, Constants.num_rounds)]])
        print("[[ MEMORY ]] - PLAYER - VARIABLES ACUMULADAS.............ACCUMULATED_IS_CORRECT:", self.accumulated_is_correct)
        print("[[ MEMORY ]] - PLAYER - VARIABLES ACUMULADAS.............PIECE_RATE_LIST:", [0 if e is None else e for e in [p.piece_rate for p in self.in_rounds(1, Constants.num_rounds)]])
        print("[[ MEMORY ]] - PLAYER - VARIABLES ACUMULADAS.............PAYOFF_LIST:", [i*j for i, j, in zip(is_correct_accumulated_list, piece_rate_list)])
        print("[[ MEMORY ]] - PLAYER - VARIABLES ACUMULADAS.............ACC_PAYOFF:", self.accumulated_payoff)
        print("[[ MEMORY ]] - PLAYER - VARIABLES ACUMULADAS.............PAYOFF:", self.payoff)
        print("[[ MEMORY ]] - END-----END-----END-----END-----END-----END-----END-----END-----END-----END-----END-----END-----END-----END-----END")

    def set_payoffs(self):
        self.payoff = self.accumulated_payoff

    def memory_admin(self):
        self.participant.vars['memory_total_is_correct'] = self.accumulated_is_correct
        self.participant.vars['memory_total_payoff'] = self.accumulated_payoff
        print("[[ MEMORY ]] - PLAYER - MEMORY_ADMIN.............ROUND NUMBER", self.round_number)
        print("[[ MEMORY ]] - PLAYER - MEMORY_ADMIN.............PVARS ARE", self.participant.vars)

