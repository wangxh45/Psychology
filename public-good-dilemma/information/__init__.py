from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'information'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    quiz1 = models.StringField(
        label='1.您以前是否做过类似的实验?',
        choices=['是', '否'],
        widget=widgets.RadioSelectHorizontal
    )
    quiz2 = models.StringField(
        label='2.您是否有注意到实验页面中出现的图片?',
        choices=['是', '否'],
        widget=widgets.RadioSelectHorizontal
    )
    quiz3 = models.StringField(
        label='3.这些图片是否对您的投资产生影响?',
        choices=['是', '否'],
        widget=widgets.RadioSelectHorizontal
    )




# FUNCTIONS
# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['quiz1', 'quiz2', 'quiz3']




page_sequence = [Demographics]
