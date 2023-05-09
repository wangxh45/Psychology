from otree.api import *



class C(BaseConstants):
    NAME_IN_URL = 'public_goods_punishment'
    PLAYERS_PER_GROUP = 4
    NUM_ROUNDS = 3
    ENDOWMENT = cu(20)
    MULTIPLIER = 1.6
    MAX_PUNISHMENT = 10
    PUNISHMENT_SCHEDULE = {
        0: 0,
        3: 1,
        6: 2,
        9: 3,
        12: 4,
        15: 5,
        18: 6,
        21: 7,
        24: 8,
        27: 9,
        30: 10,

    }


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()


def make_punishment_field(id_in_group):
    return models.IntegerField(
        min=0, max=C.MAX_PUNISHMENT, label="Punishment to player {}".format(id_in_group)
    )

class Player(BasePlayer):
    contribution = models.CurrencyField(
        min=0, max=C.ENDOWMENT, label="你将为公共池贡献多少?"
    )
    punish_p1 = make_punishment_field(1)
    punish_p2 = make_punishment_field(2)
    punish_p3 = make_punishment_field(3)
    punish_p4 = make_punishment_field(4)
    cost_of_punishing = models.CurrencyField()
    punishment_received = models.CurrencyField()


# FUNCTIONS
def creating_session(subsession):
    subsession.group_randomly()

def get_self_field(player: Player):
    return 'punish_p{}'.format(player.id_in_group)

def punishment_fields(player: Player):
    return ['punish_p{}'.format(p.id_in_group) for p in player.get_others_in_group()]

def set_payoffs(group: Group):
    players = group.get_players()
    contributions = [p.contribution for p in players]
    group.total_contribution = sum(contributions)
    group.individual_share = (
        group.total_contribution * C.MULTIPLIER / C.PLAYERS_PER_GROUP
    )
    for p in players:
        payoff_before_punishment = C.ENDOWMENT - p.contribution + group.individual_share
        self_field = get_self_field(p)
        punishments_received = [getattr(other, self_field) for other in p.get_others_in_group()]
        p.punishment_received = min(10, sum(punishments_received))
        punishments_sent = [getattr(p, field) for field in punishment_fields(p)]
        p.cost_of_punishing = sum(C.PUNISHMENT_SCHEDULE[points] for points in punishments_sent)
        p.payoff = payoff_before_punishment - p.punishment_received  - p.cost_of_punishing

def vars_for_admin_report(subsession):
    all_contributions = []
    all_payoffs = []
    for subsession in subsession.in_all_rounds():
        for group in subsession.get_groups():
            for p in group.get_players():
                contributions = p.contribution
                all_contributions.append(contributions)
                payoffs = p.payoff
                all_payoffs.append(payoffs)

    return dict(all_payoffs=all_payoffs, all_contributions=all_contributions)

# PAGES


class Contribute(Page):
    form_model = 'player'
    form_fields = ['contribution']

class WaitPage1(WaitPage):
    title_text = "请等待"
    body_text = "等待其他玩家完成决策，这可能需要一点时间"

class Punish(Page):
    form_model = 'player'
    get_form_fields = punishment_fields

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            other_players=player.get_others_in_group(), schedule=C.PUNISHMENT_SCHEDULE.items(),
        )

class WaitPage2(WaitPage):
    title_text = "请等待"
    body_text = "等待其他玩家完成决策，这可能需要一点时间"
    after_all_players_arrive = set_payoffs

class Results(Page):
    pass





page_sequence = [Contribute, WaitPage1, Punish, WaitPage2,Results]
