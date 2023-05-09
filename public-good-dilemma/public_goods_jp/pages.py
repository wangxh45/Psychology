from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class Introduction(Page):
    """Description of the game: How to play and returns expected"""

    pass


class Contribute(Page):
    """Player: Choose how much to contribute"""
  
    form_model = 'player'
    form_fields = ['contribution']
    
    timeout_seconds = 20

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'

    body_text = "等待其他成员投放"


class Results(Page):
    """Players payoff: How much each has earned"""
    
    timeout_seconds = 20

    def vars_for_template(self):
        return dict(total_earnings=self.group.total_contribution * Constants.multiplier)


page_sequence = [Introduction, Contribute, ResultsWaitPage, Results]
