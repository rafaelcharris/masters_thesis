from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Felipe Montealegre'

doc = """
Lottery
"""


class Constants(BaseConstants):
    name_in_url = 'Loteria'
    players_per_group = None
    num_rounds = 1

    endowment = 7

    lottery_payoff_win = 6
    lottery_1_payoff_loss = -2
    lottery_2_payoff_loss = -3
    lottery_3_payoff_loss = -4
    lottery_4_payoff_loss = -5
    lottery_5_payoff_loss = -6
    lottery_6_payoff_loss = -7


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    
    binary_lottery_1 = models.IntegerField()
    binary_lottery_2 = models.IntegerField()
    binary_lottery_3 = models.IntegerField()
    binary_lottery_4 = models.IntegerField()
    binary_lottery_5 = models.IntegerField()
    binary_lottery_6 = models.IntegerField()

    random_lottery = models.IntegerField()
    total_payoff = models.IntegerField()
    random_win = models.IntegerField()

    def total_payoff(self):
        self.random_lottery = random.choice([1, 2, 3, 4, 5, 6])
        self.random_win = random.choice([1, 0])
        if self.random_lottery == 1:
            if self.binary_lottery_1 == 1:
                if self.random_win == 0:
                    self.total_payoff = Constants.endowment + Constants.lottery_1_payoff_loss
                elif self.random_win == 1:
                    self.total_payoff = Constants.endowment + Constants.lottery_payoff_win
            else:
                self.total_payoff = Constants.endowment
        elif self.random_lottery == 2:
            if self.binary_lottery_2 == 1:
                if self.random_win == 0:
                    self.total_payoff = Constants.endowment + Constants.lottery_2_payoff_loss
                elif self.random_win == 1:
                    self.total_payoff = Constants.endowment + Constants.lottery_payoff_win
            else:
                self.total_payoff = Constants.endowment
        elif self.random_lottery == 3:
            if self.binary_lottery_3 == 1:
                if self.random_win == 0:
                    self.total_payoff = Constants.endowment + Constants.lottery_3_payoff_loss
                elif self.random_win == 1:
                    self.total_payoff = Constants.endowment + Constants.lottery_payoff_win
            else:
                self.total_payoff = Constants.endowment
        elif self.random_lottery == 4:
            if self.binary_lottery_4 == 1:
                if self.random_win == 0:
                    self.total_payoff = Constants.endowment + Constants.lottery_4_payoff_loss
                elif self.random_win == 1:
                    self.total_payoff = Constants.endowment + Constants.lottery_payoff_win
            else:
                self.total_payoff = Constants.endowment
        elif self.random_lottery == 5:
            if self.binary_lottery_5 == 1:
                if self.random_win == 0:
                    self.total_payoff = Constants.endowment + Constants.lottery_5_payoff_loss
                elif self.random_win == 1:
                    self.total_payoff = Constants.endowment + Constants.lottery_payoff_win
            else:
                self.total_payoff = Constants.endowment
        elif self.random_lottery == 6:
            if self.binary_lottery_6 == 1:
                if self.random_win == 0:
                    self.total_payoff = Constants.endowment + Constants.lottery_6_payoff_loss
                elif self.random_win == 1:
                    self.total_payoff = Constants.endowment + Constants.lottery_payoff_win
            else:
                self.total_payoff = Constants.endowment

        print("[[ LOTTERY ]] - PLAYER - .........................PLAYER_ID", self.id_in_group)
        print("[[ LOTTERY ]] - PLAYER - TOTAL_PAYOFF.............BINARY_LOTTERY LIST", [self.binary_lottery_1, self.binary_lottery_2, self.binary_lottery_3, self.binary_lottery_4, self.binary_lottery_5, self.binary_lottery_6])
        print("[[ LOTTERY ]] - PLAYER - TOTAL_PAYOFF.............RANDOM_LOTTERY", self.random_lottery)
        print("[[ LOTTERY ]] - PLAYER - TOTAL_PAYOFF.............RANDOM_WIN", self.random_win)
        print("[[ LOTTERY ]] - PLAYER - TOTAL_PAYOFF.............TOTAL_PAYOFF", self.total_payoff)
        print("[[ LOTTERY ]] - END-----END-----END-----END-----END-----END-----END-----END-----END-----END-----END-----END-----END-----END-----END")

    def set_payoffs(self):
        self.payoff = self.total_payoff

    def lottery_admin(self):
        self.participant.vars['lottery_total_payoff'] = self.total_payoff
        print("[[ LOTTERY  ]] - PLAYER - LOTTERY _ADMIN.............ROUND NUMBER", self.round_number)
        print("[[ LOTTERY  ]] - PLAYER - LOTTERY _ADMIN.............PVARS ARE", self.participant.vars)
