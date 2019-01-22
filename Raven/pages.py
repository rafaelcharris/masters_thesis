from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import time


class Intro_raven(Page):

    def is_displayed(self):
        return self.player.round_number == 1

    # http://otree.readthedocs.io/en/latest/timeouts.html
    def before_next_page(self):
        self.participant.vars['expiry_raven'] = time.time() + Constants.time_limit_raven


class Q1(Page):

    form_model = 'player'
    form_fields = ['is_correct_q1']

    # http://otree.readthedocs.io/en/latest/timeouts.html
    def get_timeout_seconds(self):
        return self.participant.vars['expiry_raven'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_raven'] - time.time() > 0

    def before_next_page(self):
        #self.player.variables_acumuladas()
        self.player.variables()


class Q2(Page):

    form_model = 'player'
    form_fields = ['is_correct_q2']

    # http://otree.readthedocs.io/en/latest/timeouts.html
    def get_timeout_seconds(self):
        return self.participant.vars['expiry_raven'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_raven'] - time.time() > 0

    def before_next_page(self):
        #self.player.variables_acumuladas()
        self.player.variables()


class Q3(Page):

    form_model = 'player'
    form_fields = ['is_correct_q3']

    # http://otree.readthedocs.io/en/latest/timeouts.html
    def get_timeout_seconds(self):
        return self.participant.vars['expiry_raven'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_raven'] - time.time() > 0

    def before_next_page(self):
        #self.player.variables_acumuladas()
        self.player.variables()


class Q4(Page):

    form_model = 'player'
    form_fields = ['is_correct_q4']

    # http://otree.readthedocs.io/en/latest/timeouts.html
    def get_timeout_seconds(self):
        return self.participant.vars['expiry_raven'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_raven'] - time.time() > 0

    def before_next_page(self):
        #self.player.variables_acumuladas()
        self.player.variables()


class Q5(Page):

    form_model = 'player'
    form_fields = ['is_correct_q5']

    # http://otree.readthedocs.io/en/latest/timeouts.html
    def get_timeout_seconds(self):
        return self.participant.vars['expiry_raven'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_raven'] - time.time() > 0

    def before_next_page(self):
        #self.player.variables_acumuladas()
        self.player.variables()


class Q6(Page):

    form_model = 'player'
    form_fields = ['is_correct_q6']

    # http://otree.readthedocs.io/en/latest/timeouts.html
    def get_timeout_seconds(self):
        return self.participant.vars['expiry_raven'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_raven'] - time.time() > 0

    def before_next_page(self):
        #self.player.variables_acumuladas()
        self.player.variables()


class Q7(Page):

    form_model = 'player'
    form_fields = ['is_correct_q7']

    # http://otree.readthedocs.io/en/latest/timeouts.html
    def get_timeout_seconds(self):
        return self.participant.vars['expiry_raven'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_raven'] - time.time() > 0

    def before_next_page(self):
        #self.player.variables_acumuladas()
        self.player.variables()


class Q8(Page):

    form_model = 'player'
    form_fields = ['is_correct_q8']

    # http://otree.readthedocs.io/en/latest/timeouts.html
    def get_timeout_seconds(self):
        return self.participant.vars['expiry_raven'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_raven'] - time.time() > 0

    def before_next_page(self):
        #self.player.variables_acumuladas()
        self.player.variables()


class Q9(Page):

    form_model = 'player'
    form_fields = ['is_correct_q9']

    # http://otree.readthedocs.io/en/latest/timeouts.html
    def get_timeout_seconds(self):
        return self.participant.vars['expiry_raven'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_raven'] - time.time() > 0

    def before_next_page(self):
        #self.player.variables_acumuladas()
        self.player.variables()


class Q10(Page):

    form_model = 'player'
    form_fields = ['is_correct_q10']

    # http://otree.readthedocs.io/en/latest/timeouts.html
    def get_timeout_seconds(self):
        return self.participant.vars['expiry_raven'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_raven'] - time.time() > 0

    def before_next_page(self):
        #self.player.variables_acumuladas()
        self.player.variables()


class Results_raven(Page):
    pass

    def vars_for_template(self):
        self.player.variables()
        self.player.set_payoffs()
        self.player.raven_admin()


page_sequence = [
    Intro_raven,
    Q1,
    Q2,
    Q3,
    Q4,
    Q5,
    Q6,
    Q7,
    Q8,
    Q9,
    Q10,
    Results_raven,
]
