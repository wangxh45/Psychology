from otree.api import *

doc = """
Comprehension test. If the user fails too many times, they exit.
"""


class C(BaseConstants):
    NAME_IN_URL = 'comprehension_test'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    num_failed_attempts = models.IntegerField(initial=0)
    failed_too_many = models.BooleanField(initial=False)
    quiz1 = models.StringField(
        label='1.如果其他三名玩家一共向公共账户里投入150个代币，你向公共账户里投入了50个代币，这轮结束后你的代币数是',
        choices=['150', '200', '250'],
        widget=widgets.RadioSelectHorizontal
    )
    quiz2 = models.StringField(
        label='2.如果其他三名玩家一共向公共账户里投入200个代币，你向公共账户里投入了0个代币，这轮结束后你的代币数是',
        choices=['250', '200', '150'],
        widget=widgets.RadioSelectHorizontal
    )
    quiz3 = models.StringField(
        label='3.如果其他三名玩家一共向公共账户里投入300个代币，你向公共账户里投入了100个代币，这轮结束后你的代币数是',
        choices=['200', '100', '150'],
        widget=widgets.RadioSelectHorizontal
    )




class MyPage(Page):
    form_model = 'player'
    form_fields = ['quiz1', 'quiz2', 'quiz3']

    @staticmethod
    def error_message(player:Player, values):
        # alternatively, you could make quiz1_error_message, quiz2_error_message, etc.
        # but if you have many similar fields, this is more efficient.
        solutions = dict(quiz1='150', quiz2='200', quiz3='200')

        errors = {name: '错误' for name in solutions if values[name] != solutions[name]}
        # print('errors is', errors)
        if errors:
            player.num_failed_attempts += 1
            if player.num_failed_attempts >= 10:
                player.failed_too_many = True
                # we don't return any error here; just let the user proceed to the
                # next page, but the next page is the 'failed' page that boots them
                # from the experiment.
            else:
                return errors






class Introduce(Page):
    pass

class Mypage(Page):
    pass

class Failed(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.failed_too_many

page_sequence = [Introduce, MyPage, Failed]
