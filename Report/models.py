from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from django.db import models as djmodels
from django.core.validators import EmailValidator

author = 'Felipe Montealegre'

doc = """
Your app description
"""


class UnalEmailValidator(EmailValidator):
    def validate_domain_part(self, domain_part):
        if domain_part != 'unal.edu.co':
            return False
        return True
    message = "Por favor ingrese un correo con dominio @unal.edu.co"


class Constants(BaseConstants):
    name_in_url = 'Report'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):

    def vars_for_admin_report(self):
        table_rows = []
        for player in self.get_players():
            row = player.participant.vars
            row['participant_code'] = player.participant.code
            row['treatment'] = player.participant.vars.get('treatment')
            row['consent_nombre'] = player.participant.vars.get('consent_nombre')
            row['consent_id_number'] = player.participant.vars.get('consent_id_number')
            row['sumas_total_is_correct'] = player.participant.vars.get('sumas_total_is_correct')
            row['sumas_total_payoff'] = player.participant.vars.get('sumas_total_payoff')
            row['memory_total_is_correct'] = player.participant.vars.get('memory_total_is_correct')
            row['memory_total_payoff'] = player.participant.vars.get('memory_total_payoff')
            row['dados_reporte_numero'] = player.participant.vars.get('dados_reporte_numero')
            row['dados_payoff'] = player.participant.vars.get('dados_payoff')
            row['raven_total_is_correct'] = player.participant.vars.get('raven_total_is_correct')
            row['raven_total_payoff'] = player.participant.vars.get('raven_total_payoff')
            row['lottery_total_payoff'] = player.participant.vars.get('lottery_total_payoff')

            table_rows.append(row)
        return {'table_rows': table_rows}


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    report_participant_code = models.StringField()
    report_treatment = models.StringField()
    report_consent_nombre = models.StringField()
    report_consent_id_number = models.IntegerField()
    report_sumas_total_is_correct = models.IntegerField()
    report_sumas_total_payoff = models.CurrencyField()
    report_memory_total_is_correct = models.IntegerField()
    report_memory_total_payoff = models.CurrencyField()
    report_dados_reporte_numero = models.IntegerField()
    report_dados_payoff = models.CurrencyField()
    report_raven_total_is_correct = models.IntegerField()
    report_raven_total_payoff = models.IntegerField()
    report_lottery_total_payoff = models.IntegerField()

    e_mail = djmodels.EmailField(verbose_name='Correo Electrónico', validators=[UnalEmailValidator()])

    def report_vars_for_database(self):
        self.report_participant_code = self.participant.code
        vars_fields = [
            'treatment',
            'consent_nombre',
            'consent_id_number',
            'sumas_total_is_correct',
            'sumas_total_payoff',
            'memory_total_is_correct',
            'memory_total_payoff',
            'dados_reporte_numero',
            'dados_payoff',
            'raven_total_is_correct',
            'raven_total_payoff',
            'lottery_total_payoff'
        ]

        for field in vars_fields:
            setattr(self, 'report_{}'.format(field), self.participant.vars.get(field))
        print("[[ REPORT ]] - PLAYER - REPORT_VARS_FOR_DB - PARTICIPANT_CODE", self.participant.code)
        print("[[ REPORT ]] - PLAYER - REPORT_VARS_FOR_DB - TREATMENT", self.participant.vars.get('treatment'))
        print("[[ REPORT ]] - PLAYER - REPORT_VARS_FOR_DB - CONSENT_NOMBRE", self.participant.vars.get('consent_nombre'))
        print("[[ REPORT ]] - PLAYER - REPORT_VARS_FOR_DB - CONSENT_ID", self.participant.vars.get('consent_id_number'))
        print("[[ REPORT ]] - PLAYER - REPORT_VARS_FOR_DB - SUMAS_IS_CORRECT", self.participant.vars.get('sumas_total_is_correct'))
        print("[[ REPORT ]] - PLAYER - REPORT_VARS_FOR_DB - SUMAS_T.PAYOFF", self.participant.vars.get('sumas_total_payoff'))
        print("[[ REPORT ]] - PLAYER - REPORT_VARS_FOR_DB - MEMORY_IS_CORRECT", self.participant.vars.get('memory_total_is_correct'))
        print("[[ REPORT ]] - PLAYER - REPORT_VARS_FOR_DB - MEMORY_T.PAYOFF", self.participant.vars.get('memory_total_payoff'))
        print("[[ REPORT ]] - PLAYER - REPORT_VARS_FOR_DB - DADOS_NUMERO", self.participant.vars.get('dados_reporte_numero'))
        print("[[ REPORT ]] - PLAYER - REPORT_VARS_FOR_DB - DADOS_T.PAYOFF", self.participant.vars.get('dados_payoff'))
        print("[[ REPORT ]] - PLAYER - REPORT_VARS_FOR_DB - RAVEN_T_IS_CORRECT", self.participant.vars.get('raven_total_is_correct'))
        print("[[ REPORT ]] - PLAYER - REPORT_VARS_FOR_DB - RAVEN_T.PAYOFF", self.participant.vars.get('raven_total_payoff'))
        print("[[ REPORT ]] - PLAYER - REPORT_VARS_FOR_DB - LOTTERY_T.PAYOFF", self.participant.vars.get('lottery_total_payoff'))
        print("")

