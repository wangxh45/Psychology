from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


doc = """
This is a five-period public goods game with 4 players.
"""


class Constants(BaseConstants):
    name_in_url = 'public_goods_jp'
    players_per_group = 4
    num_rounds = 12

    instructions_template = 'public_goods_jp/instructions.html'

    # """Amount allocated to each player"""
    endowment = c(100)
    multiplier = 2


class Subsession(BaseSubsession):
    def vars_for_admin_report(self):
        contributions = [
            p.contribution for p in self.get_players() if p.contribution != None
        ]
        if contributions:
            return dict(
                avg_contribution=sum(contributions) / len(contributions),
                min_contribution=min(contributions),
                max_contribution=max(contributions),
            )
        else:
            return dict(
                avg_contribution='(no data)',
                min_contribution='(no data)',
                max_contribution='(no data)',
            )


class Group(BaseGroup):
    total_contribution = models.CurrencyField()

    individual_share = models.CurrencyField()

   
    def set_payoffs(self):
        self.total_contribution = sum([p.contribution for p in self.get_players()])

        if self.total_contribution >= 200:
            self.individual_share = (
            self.total_contribution * Constants.multiplier / Constants.players_per_group
        )
        else:
            self.individual_share = 0
        for p in self.get_players():
            p.payoff = (Constants.endowment - p.contribution) + self.individual_share
        #    for round in range(1,p.round_number +1):
        #        p.sum_payoff = inpay + p.payoff


            
            


class Player(BasePlayer):
    contribution = models.CurrencyField(
        min=0,max=Constants.endowment,doc="""投入公共账户的游戏币为：""",
        label="本轮你投放的游戏币 (0 ~ 100之间的正整数)："
    )
    

