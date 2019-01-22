from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import time


class PlayerBot(Bot):

    def play_round(self):

        respuestas = [275, 172, 240, 231, 280, 266, 304, 291, 237, 224, 249, 245, 196, 370, 331, 288, 310, 232, 232,
                      318, 203, 143, 271, 194, 161, 303, 314, 288, 346, 299, 277, 330, 282, 292, 207, 222, 344, 180,
                      244, 314, 257, 238, 233, 370, 293, 176, 312, 231, 316, 377, 154, 292, 120, 233, 244, 297, 201,
                      279, 186, 146, 215, 272, 182, 266, 243, 330, 370, 79, 295, 223, 302, 195, 318, 272, 272, 307,
                      244, 267, 288, 335, 286, 207, 253, 271, 339, 267, 106, 208, 367, 294, 184, 344, 264, 210, 257,
                      218, 60, 212, 367, 272]

        respuesta = respuestas[self.player.round_number - 1]

        if self.player.round_number == 1:
            yield (pages.Intro_sumas)
            yield (pages.Sumas, {'respuesta': respuesta})
        elif (1 < self.player.round_number < 50) and (self.player.participant.vars['expiry'] - time.time() > 0.2):

            yield (pages.Sumas, {'respuesta': respuesta})
        elif self.player.round_number == 50:

            yield (pages.Sumas, {'respuesta': respuesta})
            yield (pages.Anuncio)
        elif (50 < self.player.round_number < 100) and (self.player.participant.vars['expiry'] - time.time() > 0.2):

            yield (pages.Sumas, {'respuesta': respuesta})
        elif self.player.round_number == 100:
            yield (pages.Sumas, {'respuesta': respuesta})
            yield (pages.Results_sumas)


#        if self.player.round_number == 1:
#            yield (pages.Intro_sumas)
#            yield (pages.Sumas, {'respuesta': respuesta})
#        elif (1 < self.player.round_number < 50) or (self.player.participant.vars['expiry'] - time.time() > 0):
#            yield (pages.Sumas, {'respuesta': respuesta})
#        elif self.player.round_number == 50 or (self.player.participant.vars['expiry'] - time.time() == 0):
#            yield (pages.Anuncio)
#        elif (50 < self.player.round_number < 100) or (self.player.participant.vars['expiry'] - time.time() > 0):
#            yield (pages.Sumas, {'respuesta': respuesta})
#        elif self.player.round_number == 100:
#            yield (pages.Results_sumas)

#        if self.player.round_number == 1:
#            yield (pages.Intro_sumas)
#            yield (pages.Sumas, {'respuesta': respuesta})
#        elif (1 < self.player.round_number < 50) or (self.player.participant.vars['expiry'] - time.time() > 0.1):
#            yield (pages.Sumas, {'respuesta': respuesta})
#        elif self.player.round_number == 50:
#            yield (pages.Sumas, {'respuesta': respuesta})
#            yield (pages.Anuncio)
#        elif (50 < self.player.round_number < 100) or (self.player.participant.vars['expiry'] - time.time() > 0.1):
#            yield (pages.Sumas, {'respuesta': respuesta})
#        elif self.player.round_number == 100:
#            yield (pages.Sumas, {'respuesta': respuesta})
#            yield (pages.Results_sumas)



#    def play_round(self):
#        if self.player.round_number == 1:
#            yield (pages.Intro_sumas)
#            yield (pages.Sumas, {'respuesta': 275})
#        elif self.player.round_number == 2:
#            yield (pages.Sumas, {'respuesta': 172})
#        elif self.player.round_number == 3:
#            yield (pages.Sumas, {'respuesta': 240})
#        elif self.player.round_number == 4:
#            yield (pages.Sumas, {'respuesta': 231})
#        elif self.player.round_number == 5:
#            yield (pages.Sumas, {'respuesta': 280})
#        elif self.player.round_number == 6:
#            yield (pages.Sumas, {'respuesta': 266})
#        elif self.player.round_number == 7:
#            yield (pages.Sumas, {'respuesta': 304})
#        elif self.player.round_number == 8:
#            yield (pages.Sumas, {'respuesta': 291})
#        elif self.player.round_number == 9:
#            yield (pages.Sumas, {'respuesta': 237})
#        elif self.player.round_number == 10:
#            yield (pages.Sumas, {'respuesta': 224})
#        elif self.player.round_number == 11:
#            yield (pages.Sumas, {'respuesta': 249})
#        elif self.player.round_number == 12:
#            yield (pages.Sumas, {'respuesta': 245})
#        elif self.player.round_number == 13:
#            yield (pages.Sumas, {'respuesta': 196})
#        elif self.player.round_number == 14:
#            yield (pages.Sumas, {'respuesta': 370})
#        elif self.player.round_number == 15:
#            yield (pages.Sumas, {'respuesta': 331})
#        elif self.player.round_number == 16:
#            yield (pages.Sumas, {'respuesta': 288})
#        elif self.player.round_number == 17:
#            yield (pages.Sumas, {'respuesta': 310})
#        elif self.player.round_number == 18:
#            yield (pages.Sumas, {'respuesta': 232})
#        elif self.player.round_number == 19:
#            yield (pages.Sumas, {'respuesta': 232})
#        elif self.player.round_number == 20:
#            yield (pages.Sumas, {'respuesta': 318})
#        elif self.player.round_number == 21:
#            yield (pages.Sumas, {'respuesta': 203})
#        elif self.player.round_number == 22:
#            yield (pages.Sumas, {'respuesta': 143})
#        elif self.player.round_number == 23:
#            yield (pages.Sumas, {'respuesta': 271})
#        elif self.player.round_number == 24:
#            yield (pages.Sumas, {'respuesta': 194})
#        elif self.player.round_number == 25:
#            yield (pages.Sumas, {'respuesta': 161})
#        elif self.player.round_number == 26:
#            yield (pages.Sumas, {'respuesta': 303})
#        elif self.player.round_number == 27:
#            yield (pages.Sumas, {'respuesta': 314})
#        elif self.player.round_number == 28:
#            yield (pages.Sumas, {'respuesta': 288})
#        elif self.player.round_number == 29:
#            yield (pages.Sumas, {'respuesta': 346})
#        elif self.player.round_number == 30:
#            yield (pages.Sumas, {'respuesta': 299})
#        elif self.player.round_number == 31:
#            yield (pages.Sumas, {'respuesta': 277})
#        elif self.player.round_number == 32:
#            yield (pages.Sumas, {'respuesta': 330})
#        elif self.player.round_number == 33:
#            yield (pages.Sumas, {'respuesta': 282})
#        elif self.player.round_number == 34:
#            yield (pages.Sumas, {'respuesta': 292})
#        elif self.player.round_number == 35:
#            yield (pages.Sumas, {'respuesta': 207})
#        elif self.player.round_number == 36:
#            yield (pages.Sumas, {'respuesta': 222})
#        elif self.player.round_number == 37:
#            yield (pages.Sumas, {'respuesta': 344})
#        elif self.player.round_number == 38:
#            yield (pages.Sumas, {'respuesta': 180})
#        elif self.player.round_number == 39:
#            yield (pages.Sumas, {'respuesta': 244})
#        elif self.player.round_number == 40:
#            yield (pages.Sumas, {'respuesta': 314})
#        elif self.player.round_number == 41:
#            yield (pages.Sumas, {'respuesta': 257})
#        elif self.player.round_number == 42:
#            yield (pages.Sumas, {'respuesta': 238})
#        elif self.player.round_number == 43:
#            yield (pages.Sumas, {'respuesta': 233})
#        elif self.player.round_number == 44:
#            yield (pages.Sumas, {'respuesta': 370})
#        elif self.player.round_number == 45:
#            yield (pages.Sumas, {'respuesta': 293})
#        elif self.player.round_number == 46:
#            yield (pages.Sumas, {'respuesta': 176})
#        elif self.player.round_number == 47:
#            yield (pages.Sumas, {'respuesta': 312})
#        elif self.player.round_number == 48:
#            yield (pages.Sumas, {'respuesta': 231})
#        elif self.player.round_number == 49:
#            yield (pages.Sumas, {'respuesta': 316})
#        elif self.player.round_number == 50:
#            yield (pages.Sumas, {'respuesta': 377})
#            yield (pages.Anuncio)
#        elif self.player.round_number == 51:
#            yield (pages.Sumas, {'respuesta': 154})
#        elif self.player.round_number == 52:
#            yield (pages.Sumas, {'respuesta': 292})
#        elif self.player.round_number == 53:
#            yield (pages.Sumas, {'respuesta': 120})
#        elif self.player.round_number == 54:
#            yield (pages.Sumas, {'respuesta': 233})
#        elif self.player.round_number == 55:
#            yield (pages.Sumas, {'respuesta': 244})
#        elif self.player.round_number == 56:
#            yield (pages.Sumas, {'respuesta': 297})
#        elif self.player.round_number == 57:
#            yield (pages.Sumas, {'respuesta': 201})
#        elif self.player.round_number == 58:
#            yield (pages.Sumas, {'respuesta': 279})
#        elif self.player.round_number == 59:
#            yield (pages.Sumas, {'respuesta': 186})
#        elif self.player.round_number == 60:
#            yield (pages.Sumas, {'respuesta': 146})
#        elif self.player.round_number == 61:
#            yield (pages.Sumas, {'respuesta': 215})
#        elif self.player.round_number == 62:
#            yield (pages.Sumas, {'respuesta': 272})
#        elif self.player.round_number == 63:
#            yield (pages.Sumas, {'respuesta': 182})
#        elif self.player.round_number == 64:
#            yield (pages.Sumas, {'respuesta': 266})
#        elif self.player.round_number == 65:
#            yield (pages.Sumas, {'respuesta': 243})
#        elif self.player.round_number == 66:
#            yield (pages.Sumas, {'respuesta': 330})
#        elif self.player.round_number == 67:
#            yield (pages.Sumas, {'respuesta': 370})
#        elif self.player.round_number == 68:
#            yield (pages.Sumas, {'respuesta': 79})
#        elif self.player.round_number == 69:
#            yield (pages.Sumas, {'respuesta': 295})
#        elif self.player.round_number == 70:
#            yield (pages.Sumas, {'respuesta': 223})
#        elif self.player.round_number == 71:
#            yield (pages.Sumas, {'respuesta': 302})
#        elif self.player.round_number == 72:
#            yield (pages.Sumas, {'respuesta': 195})
#        elif self.player.round_number == 73:
#            yield (pages.Sumas, {'respuesta': 318})
#        elif self.player.round_number == 74:
#            yield (pages.Sumas, {'respuesta': 272})
#        elif self.player.round_number == 75:
#            yield (pages.Sumas, {'respuesta': 272})
#        elif self.player.round_number == 76:
#            yield (pages.Sumas, {'respuesta': 307})
#        elif self.player.round_number == 77:
#            yield (pages.Sumas, {'respuesta': 244})
#        elif self.player.round_number == 78:
#            yield (pages.Sumas, {'respuesta': 267})
#        elif self.player.round_number == 79:
#            yield (pages.Sumas, {'respuesta': 288})
#        elif self.player.round_number == 80:
#            yield (pages.Sumas, {'respuesta': 335})
#        elif self.player.round_number == 81:
#            yield (pages.Sumas, {'respuesta': 286})
#        elif self.player.round_number == 82:
#            yield (pages.Sumas, {'respuesta': 207})
#        elif self.player.round_number == 83:
#            yield (pages.Sumas, {'respuesta': 253})
#        elif self.player.round_number == 84:
#            yield (pages.Sumas, {'respuesta': 271})
#        elif self.player.round_number == 85:
#            yield (pages.Sumas, {'respuesta': 339})
#        elif self.player.round_number == 86:
#            yield (pages.Sumas, {'respuesta': 267})
#        elif self.player.round_number == 87:
#            yield (pages.Sumas, {'respuesta': 106})
#        elif self.player.round_number == 88:
#            yield (pages.Sumas, {'respuesta': 208})
#        elif self.player.round_number == 89:
#            yield (pages.Sumas, {'respuesta': 367})
#        elif self.player.round_number == 90:
#            yield (pages.Sumas, {'respuesta': 294})
#        elif self.player.round_number == 91:
#            yield (pages.Sumas, {'respuesta': 184})
#        elif self.player.round_number == 92:
#            yield (pages.Sumas, {'respuesta': 344})
#        elif self.player.round_number == 93:
#            yield (pages.Sumas, {'respuesta': 264})
#        elif self.player.round_number == 94:
#            yield (pages.Sumas, {'respuesta': 210})
#        elif self.player.round_number == 95:
#            yield (pages.Sumas, {'respuesta': 257})
#        elif self.player.round_number == 96:
#            yield (pages.Sumas, {'respuesta': 218})
#        elif self.player.round_number == 97:
#            yield (pages.Sumas, {'respuesta': 160})
#        elif self.player.round_number == 98:
#            yield (pages.Sumas, {'respuesta': 212})
#        elif self.player.round_number == 99:
#            yield (pages.Sumas, {'respuesta': 367})
#        elif self.player.round_number == 100:
#            yield (pages.Sumas, {'respuesta': 272})
#            yield (pages.Results_sumas)
#        else:
#            pass
