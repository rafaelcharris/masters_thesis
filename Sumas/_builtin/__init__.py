# This file is auto-generated.
# It's used to aid autocompletion in code editors.

import otree.api

from Sumas.models import Subsession
from .. import models


class Page(otree.api.Page):
    def z_autocomplete(self):
        self.subsession = models.Subsession()
        self.group = models.Group()
        self.player = models.Player()


class WaitPage(otree.api.WaitPage):
    subsession: Subsession

    def z_autocomplete(self):
        self.subsession = models.Subsession()
        self.group = models.Group()


class Bot(otree.api.Bot):
    def z_autocomplete(self):
        self.subsession = models.Subsession()
        self.group = models.Group()
        self.player = models.Player()
