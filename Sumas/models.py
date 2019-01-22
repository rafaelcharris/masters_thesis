from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import itertools


author = 'Felipe Montealegre'

doc = """
Your app description
"""


class Constants(BaseConstants):

    name_in_url = 'Sumas'
    players_per_group = None
    num_rounds = 100
    half_way = (num_rounds / 2)

    time_limit = 60*4

    piece_rate = 1000
    nis = 0.5

    sumandos = [
        [96, 56, 00, 43, 80],
        [13, 90, 23, 44, 2],
        [85, 20, 10, 34, 91],
        [85, 70, 52, 11, 13],
        [75, 84, 81, 17, 23],
        [19, 57, 40, 97, 53],
        [8, 94, 63, 73, 66],
        [59, 82, 42, 13, 95],
        [74, 94, 12, 50, 7],
        [61, 84, 6, 10, 63],
        [38, 94, 95, 20, 2],
        [17, 28, 95, 33, 72],
        [31, 27, 36, 97, 5],
        [54, 82, 46, 97, 91],
        [97, 94, 44, 45, 51],
        [74, 74, 78, 45, 17],
        [86, 68, 81, 6, 69],
        [40, 89, 18, 61, 24],
        [76, 11, 8, 81, 56],
        [87, 88, 59, 5, 79],
        [88, 4, 3, 29, 79],
        [2, 55, 20, 4, 62],
        [40, 35, 66, 42, 88],
        [65, 56, 6, 61, 6],
        [26, 20, 75, 22, 18],
        [68, 86, 74, 34, 41],
        [97, 87, 75, 52, 3],
        [66, 72, 27, 42, 81],
        [81, 87, 80, 89, 9],
        [13, 84, 38, 76, 88],
        [57, 50, 45, 68, 57],
        [37, 91, 93, 86, 23],
        [42, 92, 88, 58, 2],
        [84, 74, 39, 83, 12],
        [10, 10, 25, 99, 63],
        [41, 41, 53, 62, 25],
        [88, 27, 64, 92, 73],
        [89, 36, 21, 18, 16],
        [66, 18, 92, 00, 68],
        [92, 76, 3, 69, 74],
        [50, 62, 14, 34, 97],
        [65, 92, 23, 51, 7],
        [64, 32, 47, 74, 16],
        [90, 98, 83, 10, 89],
        [61, 75, 45, 90, 22],
        [23, 17, 58, 76, 2],
        [23, 88, 98, 40, 63],
        [20, 65, 70, 66, 10],
        [62, 6, 69, 94, 85],
        [85, 97, 56, 82, 57],
        [19, 27, 52, 13, 43],
        [11, 27, 74, 92, 88],
        [19, 31, 21, 44, 5],
        [82, 25, 31, 79, 16],
        [3, 49, 76, 50, 66],
        [91, 31, 98, 54, 23],
        [22, 54, 45, 77, 3],
        [66, 39, 30, 61, 83],
        [18, 4, 50, 77, 37],
        [4, 22, 71, 40, 9],
        [31, 52, 79, 48, 5],
        [74, 92, 22, 67, 17],
        [77, 45, 2, 50, 8],
        [49, 62, 78, 62, 15],
        [39, 36, 18, 87, 63],
        [95, 86, 21, 35, 93],
        [58, 97, 72, 62, 81],
        [3, 15, 39, 19, 3],
        [3, 85, 37, 78, 92],
        [46, 15, 53, 86, 23],
        [17, 78, 54, 97, 56],
        [39, 9, 7, 48, 92],
        [75, 28, 51, 88, 76],
        [75, 75, 24, 18, 80],
        [74, 74, 16, 58, 50],
        [95, 53, 20, 83, 56],
        [39, 36, 86, 65, 18],
        [36, 71, 9, 78, 73],
        [37, 76, 49, 41, 85],
        [69, 49, 92, 51, 74],
        [69, 85, 58, 32, 42],
        [40, 14, 58, 2, 93],
        [64, 59, 42, 86, 2],
        [34, 39, 74, 74, 50],
        [84, 47, 52, 75, 81],
        [50, 72, 42, 37, 66],
        [16, 11, 25, 29, 25],
        [13, 4, 53, 90, 48],
        [93, 57, 50, 96, 71],
        [88, 94, 15, 84, 13],
        [21, 45, 28, 21, 69],
        [85, 67, 81, 22, 89],
        [69, 49, 37, 45, 64],
        [35, 2, 46, 98, 29],
        [51, 70, 17, 99, 20],
        [19, 50, 54, 76, 19],
        [15, 25, 11, 15, 94],
        [25, 47, 45, 26, 69],
        [98, 63, 93, 80, 33],
        [68, 57, 22, 47, 78],
    ]


class Subsession(BaseSubsession):

    def creating_session(self):

        #carga de sumandos
        for p in self.get_players():
            p.sumando_1 = Constants.sumandos[self.round_number - 1][0]
            p.sumando_2 = Constants.sumandos[self.round_number - 1][1]
            p.sumando_3 = Constants.sumandos[self.round_number - 1][2]
            p.sumando_4 = Constants.sumandos[self.round_number - 1][3]
            p.sumando_5 = Constants.sumandos[self.round_number - 1][4]
            p.solucion = p.sumando_1 + p.sumando_2 + p.sumando_3 + p.sumando_4 + p.sumando_5
            print("[[ SUMAS ]] - in sumandos @@@@@@@@@@@@---------------@@@@@@@@@@@ sumandos are", p.sumando_1, p.sumando_2,
                  p.sumando_3, p.sumando_4, p.sumando_5)
        # inicializacion de tratamientos
        if self.round_number == 1:
            treatment = itertools.cycle(['pre_treatment', 'pre_treatment', 'pre_treatment', 'pre_treatment'])
            for p in self.get_players():
                p.participant.vars['treatment'] = next(treatment)
                print("[[ SUMAS ]] - @@@@@@@@@@@@---------------@@@@@@@@@@@ treatment is", p.participant.vars['treatment'])
                print("[[ SUMAS ]] - @@@@@@@@@@@@---------------@@@@@@@@@@@ piece_rate is", p.piece_rate)
                print("")
        elif self.round_number == Constants.half_way + 1:
            treatment = itertools.cycle(['poor_nonis', 'poor_nis', 'rich_nonis', 'rich_nis'])
            for p in self.get_players():
                p.participant.vars['treatment'] = next(treatment)
                print("[[ SUMAS ]] - @@@@@@@@@@@@---------------@@@@@@@@@@@ treatment is", p.participant.vars['treatment'])
                print("[[ SUMAS ]] - @@@@@@@@@@@@---------------@@@@@@@@@@@ piece_rate is", p.piece_rate)
                print("")

        # cambio de piece_rate y de treatment(para mostrar en database) de acuerdo a tratameintos + Wealth shock
        for p in self.get_players():
            if p.participant.vars['treatment'] == 'pre_treatment':
                p.piece_rate = Constants.piece_rate
                p.treatment = p.participant.vars.get('treatment')
            elif p.participant.vars['treatment'] == 'rich_nonis':
                p.piece_rate = Constants.piece_rate
                p.treatment = p.participant.vars.get('treatment')
            elif p.participant.vars['treatment'] == 'rich_nis':
                p.piece_rate = int(Constants.piece_rate * Constants.nis)
                p.treatment = p.participant.vars.get('treatment')
            elif p.participant.vars['treatment'] == 'poor_nonis':
                p.piece_rate = Constants.piece_rate
                p.treatment = p.participant.vars.get('treatment')
            elif p.participant.vars['treatment'] == 'poor_nis':
                p.piece_rate = int(Constants.piece_rate * Constants.nis)
                p.treatment = p.participant.vars.get('treatment')
            print("[[ SUMAS ]] - @@@@@ participant is ", [p.participant.code])
        print("[[ SUMAS ]] - @@@@@ round number is ", p.round_number)
        print("[[ SUMAS ]] - @@@@@ tratamientos are", p.participant.vars['treatment'])
        print("[[ SUMAS ]] - @@@@@ p.treatment is ", p.treatment)
        print("[[ SUMAS ]] - @@@@@ piece rates are ", p.piece_rate)
        print("")


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    treatment = models.StringField()
    piece_rate = models.IntegerField()

    sumando_1 = models.IntegerField()
    sumando_2 = models.IntegerField()
    sumando_3 = models.IntegerField()
    sumando_4 = models.IntegerField()
    sumando_5 = models.IntegerField()

    solucion = models.IntegerField()
    respuesta = models.IntegerField(min=1, max=500)

    is_correct = models.IntegerField()

    accumulated_is_correct = models.IntegerField()
    total_is_correct = models.IntegerField()

    accumulated_payoff = models.IntegerField()
    total_payoff = models.IntegerField()

    def variables_acumuladas(self):

        print("[[ SUMAS ]] - PLAYER - VARIABLES ACUMULADAS.............ROUND NUMBER", self.round_number)
        print("[[ SUMAS ]] - PLAYER - VARIABLES ACUMULADAS.............PLAYER_ID", self.id_in_group)
        print("[[ SUMAS ]] - PLAYER - VARIABLES ACUMULADAS.............TRATAMIENTO", self.treatment)
        self.is_correct = 0
        self.accumulated_is_correct = 0
        self.accumulated_is_correct = sum(filter(None, [p.is_correct for p in self.in_previous_rounds()]))

        is_correct_accumulated_list_1 = [0 if e is None else e for e in [p.is_correct for p in self.in_rounds(1, Constants.half_way)]]
        is_correct_accumulated_list_2 = [0 if e is None else e for e in [p.is_correct for p in self.in_rounds(Constants.half_way + 1, Constants.num_rounds - 1)]]
        piece_rate_accumulated_list_1 = [0 if e is None else e for e in [p.piece_rate for p in self.in_rounds(1, Constants.half_way)]]
        piece_rate_accumulated_list_2 = [0 if e is None else e for e in [p.piece_rate for p in self.in_rounds(Constants.half_way + 1, Constants.num_rounds - 1)]]

        if (self.participant.vars['treatment'] == 'pre_treatment') or (self.participant.vars['treatment'] == 'rich_nonis') or (self.participant.vars['treatment'] == 'rich_nis'):
            if 1 <= self.round_number <= Constants.half_way:
                self.accumulated_payoff = sum(i * j for i, j, in zip(is_correct_accumulated_list_1, piece_rate_accumulated_list_1)) + sum(i * j for i, j, in zip(is_correct_accumulated_list_2, piece_rate_accumulated_list_2))
            elif Constants.half_way < self.round_number <= Constants.num_rounds:
                self.accumulated_payoff = sum(i * j for i, j, in zip(is_correct_accumulated_list_1, piece_rate_accumulated_list_1)) + (sum(i * j for i, j, in zip(is_correct_accumulated_list_2, piece_rate_accumulated_list_2)))
        elif (self.participant.vars['treatment'] == 'poor_nonis') or (self.participant.vars['treatment'] == 'poor_nis'):
            if 1 <= self.round_number <= Constants.half_way:
                self.accumulated_payoff = sum(i * j for i, j, in zip(is_correct_accumulated_list_1, piece_rate_accumulated_list_1)) + sum(i * j for i, j, in zip(is_correct_accumulated_list_2, piece_rate_accumulated_list_2))
            elif Constants.half_way < self.round_number <= Constants.num_rounds:
                self.accumulated_payoff = int(sum(i * j for i, j, in zip(is_correct_accumulated_list_1, piece_rate_accumulated_list_1)) / 2) + (sum(i * j for i, j, in zip(is_correct_accumulated_list_2, piece_rate_accumulated_list_2)))

        print([p.is_correct for p in self.in_previous_rounds()])
        print("[[ SUMAS ]] - IN PREVIOUS ROUNDS LIST", self.in_previous_rounds())
        print("[[ SUMAS ]] - IN PREVIOUS ROUNDS IS_CORRECT", [p.is_correct for p in self.in_previous_rounds()])
        print("[[ SUMAS ]] - IN PREVIOUS ROUNDS PIECE_RATE", [p.piece_rate for p in self.in_previous_rounds()])
        print("[[ SUMAS ]] - IN PREVIOUS ROUNDS IS_CORRECT_ACCUMULATED_LIST +", is_correct_accumulated_list_1)
        print("[[ SUMAS ]] - IN PREVIOUS ROUNDS PIECE_RATE_ACCUMULATED_LIST +", piece_rate_accumulated_list_1)
        print("[[ SUMAS ]] - IN PREVIOUS ROUNDS ACCUMULATED_PAYOFF", self.accumulated_payoff)
        print("")
        print("")
        print("")

    def variables_totales(self):

        print("[[ SUMAS ]] - PLAYER - VARIABLES TOTALES.............ROUND NUMBER", self.round_number)
        print("[[ SUMAS ]] - PLAYER - VARIABLES TOTALES.............PLAYER_ID", self.id_in_group)
        print("[[ SUMAS ]] - PLAYER - VARIABLES TOTALES.............TRATAMIENTO", self.treatment)

        if self.respuesta == self.solucion:
            self.is_correct = 1
        else:
            self.is_correct = 0

        self.total_is_correct = 0
        self.total_is_correct = sum(filter(None, [p.is_correct for p in self.in_all_rounds()]))

        is_correct_total_list_1 = [0 if e is None else e for e in [p.is_correct for p in self.in_rounds(1, Constants.half_way)]]
        is_correct_total_list_2 = [0 if e is None else e for e in [p.is_correct for p in self.in_rounds(Constants.half_way + 1, Constants.num_rounds)]]
        piece_rate_total_list_1 = [0 if e is None else e for e in [p.piece_rate for p in self.in_rounds(1, Constants.half_way)]]
        piece_rate_total_list_2 = [0 if e is None else e for e in [p.piece_rate for p in self.in_rounds(Constants.half_way + 1, Constants.num_rounds)]]

        if (self.participant.vars['treatment'] == 'pre_treatment') or (self.participant.vars['treatment'] == 'rich_nonis') or (self.participant.vars['treatment'] == 'rich_nis'):
            if 1 <= self.round_number <= Constants.half_way:
                self.total_payoff = sum(i*j for i, j, in zip(is_correct_total_list_1, piece_rate_total_list_1)) + sum(i*j for i, j, in zip(is_correct_total_list_2, piece_rate_total_list_2))
            elif Constants.half_way < self.round_number <= Constants.num_rounds:
                self.total_payoff = sum(i*j for i, j, in zip(is_correct_total_list_1, piece_rate_total_list_1)) + sum(i*j for i, j, in zip(is_correct_total_list_2, piece_rate_total_list_2))
        elif (self.participant.vars['treatment'] == 'poor_nonis') or (self.participant.vars['treatment'] == 'poor_nis'):
            if 1 <= self.round_number <= Constants.half_way:
                self.total_payoff = sum(i*j for i, j, in zip(is_correct_total_list_1, piece_rate_total_list_1)) + sum(i*j for i, j, in zip(is_correct_total_list_2, piece_rate_total_list_2))
            elif Constants.half_way < self.round_number <= Constants.num_rounds:
                self.total_payoff = int(sum(i*j for i, j, in zip(is_correct_total_list_1, piece_rate_total_list_1))/2) + int(sum(i*j for i, j, in zip(is_correct_total_list_2, piece_rate_total_list_2)))

        self.payoff = 0

        print("[[ SUMAS ]] - IN CURRENT ROUND IS_CORRECT_TOTAL_LIST_1", is_correct_total_list_1)
        print("[[ SUMAS ]] - IN CURRENT ROUND IS_CORRECT_TOTAL_LIST_2", is_correct_total_list_2)
        print("[[ SUMAS ]] - IN CURRENT ROUND, total_payoff is", self.total_payoff)
        print("[[ SUMAS ]] - IN CURRENT ROUND, payoff is", self.payoff)
        print("[[ SUMAS ]] - END-----END-----END-----END-----END-----END-----END-----END-----END-----END-----END-----END-----END-----END-----END")

    def set_payoffs(self):
        self.payoff = self.total_payoff
        print("[[ SUMAS ]] - PLAYER - SET_PAYOFFS.............ROUND NUMBER", self.round_number)
        print("[[ SUMAS ]] - PLAYER - SET_PAYOFFS.............PAYOFF", self.payoff)

    def sumas_admin(self):
        self.participant.vars['sumas_total_is_correct'] = self.total_is_correct
        self.participant.vars['sumas_total_payoff'] = self.total_payoff
        print("[[ SUMAS ]] - PLAYER - SUMAS_ADMIN.............ROUND NUMBER", self.round_number)
        print("[[ SUMAS ]] - PLAYER - SUMAS_ADMIN.............VARS ARE", self.participant.vars)
        print("[[ SUMAS ]] - PLAYER - SUMAS_ADMIN.............pvars SUMAS_TOTAL_IS_CORRECT", self.participant.vars['sumas_total_is_correct'])
        print("[[ SUMAS ]] - PLAYER - SUMAS_ADMIN.............pvars SUMAS_PAYOFF", self.participant.vars['sumas_total_payoff'])
