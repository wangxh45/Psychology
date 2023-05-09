from otree.api import *



class C(BaseConstants):
    NAME_IN_URL = 'dz'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def make_q(label):
    return models.IntegerField(label=label, choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelect, blank=True)


class Player(BasePlayer):
     a1 = make_q('我感到同情')
     a2 = make_q('我感到怜悯')
     a3 = make_q('我心肠软了')
     a4 = make_q('我感受到体贴 ')
     a5 = make_q('我感受到了温暖')
     a6 = make_q('我被感动了')



     b1 = make_q('1.当阅读材料的时候， 你在多大程度上想象材料中的场景？（1=没有想象， 7=完全想象）')
     b2 = make_q('2.当阅读材料的时候， 你在多大程度上保持客观的态度？（1=完全不客观， 7=非常客观）')
     b3 = make_q('3.当阅读材料的时候， 你在多大程度上关注了材料内容以外的事物？（1=完全不关注， 7=完全关注） ')






class Survey(Page):
    form_model = 'player'
    form_fields = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6']

class Survey2(Page):
    form_model = 'player'
    form_fields = ['b1', 'b2', 'b3']

class ResultsWaitPage2(WaitPage):
    wait_for_all_groups = True
    body_text = "等待其他玩家进入"

class Informed(Page):
    pass
page_sequence = [ResultsWaitPage2, Informed, Survey, Survey2]