from otree.api import Currency as c, currency_range, expect, Bot
from . import *


class PlayerBot(Bot):
    def play_round(self):

        yield Demographics, dict(age=24, gender='Male')



        for value in [self.player.crt_bat, self.player.payoff]:
            expect(value, '!=', None)
