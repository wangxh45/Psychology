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


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'q_dictator'
    players_per_group = 4
    num_rounds = 1
    
    instructions_template = 'q_dictator/instructions.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    
    
    give1 = models.CurrencyField(min=0,label="プレイヤーAへいくら与えるか記入してください。")
    give2 = models.CurrencyField(min=0,label="プレイヤーBへいくら与えるか記入してください。")
    give3 = models.CurrencyField(min=0,label="プレイヤーCへいくら与えるか記入してください。")
    
    def set_payoffs(self):
        self.payoff = self.participant.vars['last']
    
   
   
    #Aは損失者から損失者、Bは損失者から非損失者、Cは非損失者から損失者、Dは非損失者から非損失者への剰余額。
    #maxで上半分と下半分それぞれのgiveの和が公共財ゲームでの獲得利得を超えないようにしないとだめ。
    #自分が非損失者か損失者かでラベル
    
    
    
    
