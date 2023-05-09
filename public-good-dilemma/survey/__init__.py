from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    phone = models.IntegerField(label='您的电话号码是多少?')




# FUNCTIONS
# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['phone']




page_sequence = [Demographics]
