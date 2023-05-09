from otree.api import *



class C(BaseConstants):
    NAME_IN_URL = 'c_t'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def make_q(label):
    return models.IntegerField(label=label, choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelect)


class Player(BasePlayer):
    q1 = make_q('1.我相信好的伙伴能使你战胜一切对手')
    q2 = make_q('2.与大家一起做事情让我很愉快')
    q3 = make_q('3.在与他人共同完成任务时，我能够征求和综合大家的意见')
    q4 = make_q('4.一个人想要取得好成绩，必须依靠他人帮助')
    q5 = make_q('5.在做事情时，我喜欢与他人一同做')
    q6 = make_q('6.合作时，我通常会考虑双方利益')
    q7 = make_q('7.任何事情的完成都离不开他人帮助与合作')
    q8 = make_q('8.我喜欢与他人合作以获得共同的成功')
    q9 = make_q('9.在处理事情时，我一般能考虑多方的意见')
    q10 = make_q('10.为了成功，一个人必须与他人合作')
    q11 = make_q('11.我相信合作比竞争更有助与提高成绩')
    q12 = make_q('12.一起做事时，我通常能够站在他人的立场上考虑他人的利益')
    q13 = make_q('13.与别人共同努力是获取成功的最佳方法')




class Survey(Page):
    form_model = 'player'
    form_fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13']




page_sequence = [Survey]
