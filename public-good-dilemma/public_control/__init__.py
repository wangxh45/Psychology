from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'public_control'
    PLAYERS_PER_GROUP = 4
    NUM_ROUNDS = 12
    ENDOWMENT = cu(100)
    MULTIPLIER = 2.0



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()


class Player(BasePlayer):
    contribution = models.CurrencyField(
        min=0, max=C.ENDOWMENT, label="你将向公共账户贡献多少：?", blank=False
    )


# FUNCTIONS
def set_payoffs(group: Group):

    players = group.get_players()
    contributions = [p.contribution for p in players]
    group.total_contribution = sum(contributions)
    group.individual_share = (
        group.total_contribution * C.MULTIPLIER / C.PLAYERS_PER_GROUP
    )
    if group.total_contribution < 200:
        group.individual_share = 0
        pass
    for p in players:
        p.payoff = C.ENDOWMENT - p.contribution + group.individual_share

def creating_session(subsession):
    subsession.group_randomly(fixed_id_in_group=True)







# PAGES


class Contribute(Page):
    timeout_seconds = 60
    form_model = 'player'
    form_fields = ['contribution']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs

class Results(Page):
    pass

page_sequence = [Contribute, ResultsWaitPage, Results]
