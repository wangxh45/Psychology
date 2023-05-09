from otree.api import *


doc = """
group by arrival time, but in each round assign to a new partner.
"""


class C(BaseConstants):
    NAME_IN_URL = 'gbat_new_partners'
    PLAYERS_PER_GROUP = 4
    NUM_ROUNDS = 3
    ENDOWMENT = cu(100)
    MULTIPLIER = 2.0

class Player(BasePlayer):
    contribution = models.CurrencyField(
        min=0, max=C.ENDOWMENT, label="你将向公共账户贡献多少：?", blank=False)

class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    session = subsession.session
    session.past_groups = []


def group_by_arrival_time_method(subsession: Subsession, waiting_players):
    session = subsession.session

    import itertools

    # this generates all possible pairs of waiting players
    # and checks if the group would be valid.
    for possible_group in itertools.combinations(waiting_players, 4):
        # use a set, so that we can easily compare even if order is different
        # e.g. {1, 2} == {2, 1}
        pair_ids = set(p.id_in_subsession for p in possible_group)
        # if this pair of players has not already been played
        if pair_ids not in session.past_groups:
            # mark this group as used, so we don't repeat it in the next round.
            session.past_groups.append(pair_ids)
            # in this function,
            # 'return' means we are creating a new group with this selected pair
            return possible_group


class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()


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

#pages

class ResultsWaitPage(WaitPage):
    group_by_arrival_time = True
    body_text = "等待将与其他玩家随机配对"


class MyPage(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(partner=player.get_others_in_group()[0])


class Contribute(Page):
    # timeout_seconds = 60
    form_model = 'player'
    form_fields = ['contribution']
    # @staticmethod
    # def vars_for_template(player):
    #     return dict(
    #         image_path='eye/{}.png'.format(player.round_number)
    #     )

class ResultsWaitPage2(WaitPage):
    after_all_players_arrive = set_payoffs

class Results(Page):
    pass

page_sequence = [ResultsWaitPage, MyPage, Contribute, ResultsWaitPage2, Results]
