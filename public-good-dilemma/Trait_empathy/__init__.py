from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'Survey2'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def make_q(label):
    return models.IntegerField(label=label, choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelect, blank=True)


class Player(BasePlayer):
     c1 = make_q('1.我相信好的伙伴能使你战胜一切对手')
     c2 = make_q('2.与大家一起做事情让我很愉快')
     c3 = make_q('3.在与他人共同完成任务时，我能够征求和综合大家的意见')
     c4 = make_q('4.一个人要想取得好成绩，必须依靠他人帮助')
     c5 = make_q('5.在做事情时，我喜欢与他人一同做')
     c6 = make_q('6.合作时，我通常会考虑双方利益')
     c7 = make_q('7.任何事情的完成都离不开他人帮助与合作')
     c8 = make_q('8.我喜欢与他人合作以获得共同的成功')
     c9 = make_q('9.在处理事情时，我一般都能考虑多方的意见')
     c10 = make_q('10.为了成功，一个人必须与他人合作')
     c11 = make_q('11.我相信合作比竞争更有助于提高成绩')
     c12 = make_q('12.一起做事时，我通常能够站在他人的立场上考虑他人的利益')
     c13 = make_q('13.与别人共同努力是获取成功的最佳方法')


     e1 = make_q('1.对那些比我不幸的人， 我经常有心软和关怀的感觉 ')
     e2 = make_q('2.有时候当其他人有困难或问题时，我不为他们难过')
     e3 = make_q('3.我的确会投入小说人物中的感情世界 ')
     e4 = make_q('4.在紧急状况中，我感到担忧、害怕而难以平静 ')
     e5 = make_q('5.看电影或看戏时，我通常是旁观的，而且不经常全心投入')
     e6 = make_q('6.在做决定前，我试着从争论中去看每个人的立场是什么')
     e7 = make_q('7.当我看到有人被别人利用时，我有点感到想要保护他们')
     e8 = make_q('8.当我处在非常激动的情况中时，我往往会感到无依无靠，不知如何是好 ')
     e9 = make_q('9.有时候我从朋友的观点来看待事情，以便更了解他/她们')
     e10 = make_q('10.对我来说全心投入一本好书或一部电影中是很少有的事')
     e11 = make_q('11.其他人的不幸通常不会带给我很大的烦忧')
     e12 = make_q('12.看完电影之后，我会觉得自己好像是剧中的某一个角色')
     e13 = make_q('13.处在紧张情绪的状况中，我会惊慌害怕')
     e14 = make_q('14.当我看到有人受到不公平的对待时，我有时并不感到非常同情他/她们')
     e15 = make_q('15.我相信问题都有两面观点，我会从不同观点来看待问题')
     e16 = make_q('16.我认为自己是一个相当软心肠的人')
     e17 = make_q('17.当我观赏一部好电影时，我很容易站在某个主角的立场去感受他/她的心情')
     e18 = make_q('18.在紧急状况中，我紧张得几乎无法控制自己')
     e19 = make_q('19.当我对一个人生气时我通常会试着去想一下他/她的立场')
     e20 = make_q('20.当我阅读一篇引人的故事或小说时，我想象如果故事中的事件发生在我身上，我会感觉怎么样')
     e21 = make_q('21.当我看到有人发生意外急需帮助我紧张得几乎精神崩溃')
     e22 = make_q('22.在批评别人前，我会试着想象假如我处在他/她的情况，我的感受如何')

     gender = models.StringField(
        label='1.你的性别是?',
        choices=['男', '女'],
        widget=widgets.RadioSelectHorizontal
        )
     dushen = models.StringField(
         label='2.是否是独生子女?',
         choices=['是', '否'],
         widget=widgets.RadioSelectHorizontal
     )
     age = models.StringField(
         label='3.你的年龄是?',
     )



class Survey(Page):
    form_model = 'player'
    form_fields = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'c11', 'c12', 'c13']

class Survey2(Page):
    form_model = 'player'
    form_fields = ['e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'e10', 'e11', 'e12', 'e13' , 'e14',
                   'e15', 'e16', 'e17', 'e18', 'e19', 'e20', 'e21', 'e22']


class Demographics(Page):
    form_model = 'player'
    form_fields = ['gender', 'dushen', 'age']

class Inform(Page):
    pass
page_sequence = [Inform, Survey, Survey2, Demographics]