from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Felipe Montealegre'

doc = """
Question
"""


class Constants(BaseConstants):
    name_in_url = 'Question'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    sexo = models.CharField(
        choices=['Masculino', 'Femenino', 'Otro'],
        verbose_name='¿Cuál es su sexo?',
#        widget=widgets.RadioSelect()
    )

    edad = models.PositiveIntegerField(
        verbose_name='¿Cuál es su edad?',
        min=18, max=125
    )

    estado_civil = models.CharField(
        choices=['Soltera/o', 'Casada/o', 'Unión Marital de Hecho (Unión libre)', 'Viuda/o'],
        verbose_name='¿Cuál es su estado civil?',
#        widget=widgets.RadioSelect()
    )

    carrera = models.StringField(
        verbose_name='¿En que carrera está usted matriculado?'
    )

    matricula = models.IntegerField(
        verbose_name='¿Cuantas matrículas ha pagado contando la de este semestre?'
    )

    estrato = models.IntegerField(
        choices=[
            (1, 'Estrato 1'),
            (2, 'Estrato 2'),
            (3, 'Estrato 3'),
            (4, 'Estrato 4'),
            (5, 'Estrato 5'),
            (6, 'Estrato 6'),
        ],
        verbose_name='De acuerdo a las facturas de sus servicios públicos, ¿cuál es el estrato de la vivienda actual donde reside?',
#        widget=widgets.RadioSelect()
    )

    ingreso = models.IntegerField(
        choices=[
            (0, 'Menos de 1 salario mínimo'),
            (1, '1 salarios mínimos'),
            (2, '2 salarios mínimos'),
            (3, '3 salarios mínimos'),
            (4, '4 salarios mínimos'),
            (5, '5 salarios mínimos'),
            (6, '6 salarios mínimos'),
            (7, 'Más de 6 salarios mínimos'),
        ],
        verbose_name='¿Cuál es el valor aproximado de sus ingresos mensuales en Salarios Mínimos (SMMLV)',
#        widget=widgets.RadioSelect()
    )

    localidad = models.IntegerField(
        choices=[
            (1, 'Kennedy'),
            (2, 'Suba'),
            (3, 'Engativá'),
            (4, 'Ciudad Bolívar'),
            (5, 'Bosa'),
            (6, 'Usaquén'),
            (7, 'San Cristobal'),
            (8, 'Rafael Uribe'),
            (9, 'Fontibón'),
            (10, 'Usme'),
            (11, 'Puente Aranda'),
            (12, 'Barrios Unidos'),
            (13, 'Tunjuelito'),
            (14, 'Teusaquillo'),
            (15, 'Chapinero'),
            (16, 'Antonio Nariño'),
            (17, 'Santa Fe'),
            (18, 'Los Mártires'),
            (19, 'La Candelaria'),
            ],
        verbose_name='¿En que localidad usted reside?',
#        widget=widgets.RadioSelect()
    )

    edu_padre = models.CharField(
        choices=['Ninguno', 'Primaria', 'Bachillerato', 'Algún semestre universitario, pero no graduado', 'Técnico', 'Universitario', 'Posgrado'],
        verbose_name='¿Cuál es el nivel de educación de su padre?',
#        widget=widgets.RadioSelect()
    )

    edu_madre = models.CharField(
        choices=['Ninguno', 'Primaria', 'Bachillerato', 'Algún semestre universitario, pero no graduado', 'Técnico', 'Universitario', 'Posgrado'],
        verbose_name='¿Cuál es el nivel de educación de su madre?',
#        widget=widgets.RadioSelect()
    )

    peso = models.IntegerField(
        verbose_name='¿Cúal es su peso en kilogramos'
    )

    altura = models.IntegerField(
        verbose_name='¿Cúal es su altura en centimetros'
    )

    fehr_1 = models.IntegerField(
        choices=[1, 2, 3, 4, 5,])

    fehr_2 = models.IntegerField(
        choices=[1, 2, 3, 4, 5,])

#    fehr_1 = models.IntegerField(
#        choices=[
#            (1, '1'),
#            (2, '2'),
#            (3, '3'),
#            (4, '4'),
#            (5, '5'),
#        ],
#        label= ' ¿Cómo se considera usted? Normalmente ¿es usted una persona totalmente dispuesta a tomar riesgos o'
#               ' intenta evitar tomar riesgos? Por favor conteste usando la siguiente escala de uno (1) a cinco (5), donde'
#               ' uno (1) indica “totalmente dispuesto a tomar riesgos” y cinco (1) “Totalmente contrario a tomar riesgos”',
#        widget=widgets.RadioSelectHorizontal
#    )
#
#    fehr_2 = models.IntegerField(
#        choices=[
#            (1, '1'),
#            (2, '2'),
#            (3, '3'),
#            (4, '4'),
#            (5, '5'),
#        ],
#        label= 'Normalmente ¿es usted una persona totalmente dispuesta a tomar riesgos de carácter financiero o intenta'
#               ' evitar tomar riesgos financieros? Por favor conteste usando la siguiente escala de uno (1) a cinco (5), donde'
#               ' uno (1) indica “totalmente dispuesto a tomar riesgos” y cinco (5) “Totalmente contrario a tomar riesgos”',
#        widget=widgets.RadioSelectHorizontal
#    )


    seicientos = models.CharField(
        choices=['No tendría dificultad', 'Tendría alguna dificultad pero lo conseguiría', 'No sé si lo conseguiría', 'Definitivamente, no lo conseguiría'],
        verbose_name='Si tuviera que conseguir 600mil pesos en una semana para enfrentar un gasto no planeado, ¿qué tanta dificultad cree que tendría en conseguir el dinero?',
        widget=widgets.RadioSelect()
    )

    #def question_admin(self):
    #    self.participant.vars['consent_nombre'] = self.nombre
    #    self.participant.vars['consent_id_number'] = self.id_number
    #    print("[[ CONSENT ]] - PLAYER - CONSENT_ADMIN.............ROUND NUMBER", self.round_number)
    #    print("[[ CONSENT ]] - PLAYER - CONSENT_ADMIN.............PVARS ARE", self.participant.vars)

