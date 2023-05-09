from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'public_goods_simple_eye'
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
    # quiz1 = models.StringField(
    #     label='1.您以前是否做过类似的实验?',
    #     choices=['是', '否'],
    #     widget=widgets.RadioSelectHorizontal
    # )
    # quiz2 = models.StringField(
    #     label='2.您是否有注意到实验页面中出现的图片?',
    #     choices=['是', '否'],
    #     widget=widgets.RadioSelectHorizontal
    # )
    # quiz3 = models.StringField(
    #     label='3.这些图片是否对您的投资产生影响?',
    #     choices=['是', '否'],
    #     widget=widgets.RadioSelectHorizontal
    # )


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

class Picture(Page):
    timeout_seconds = 3
    @staticmethod
    def vars_for_template(player):
        return dict(
            image_path='eye/{}.png'.format(player.round_number)
        )

class Contribute(Page):
    timeout_seconds = 60
    form_model = 'player'
    form_fields = ['contribution']
    @staticmethod
    def vars_for_template(player):
        return dict(
            image_path='eye/{}.png'.format(player.round_number)
        )


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs


class Results(Page):
    pass

class ResultsWaitPage2(WaitPage):
    wait_for_all_groups = True
    body_text = "等待与其他玩家随机配对"



page_sequence = [Picture, Contribute, ResultsWaitPage, Results, ResultsWaitPage2]
