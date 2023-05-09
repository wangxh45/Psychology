from otree.api import *

doc = """Big 5 personality test"""


class C(BaseConstants):
    NAME_IN_URL = 'Survey2'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def make_q(label):
    return models.IntegerField(label=label, choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelect, blank=True)


class Player(BasePlayer):
     mach1 = make_q('至善是可能的。')
     mach2 = make_q('诚实永远是最好的策略。')
     mach3 = make_q('绝大数人都是勇敢的。')
     mach4 = make_q('绝大多数成功者都过着干净、有道德的生活。')
     mach5 = make_q('如果想让别人为你做事，最好告诉他真实原因，而不是那些最能影响他的原因。')
     mach6 = make_q('身患疾病无法治愈的人应该有权选择无痛苦地死亡。')
     mach7 = make_q('讨好大人物是明智的。')
     mach8 = make_q('总的来说，除非被迫，否则人们不会努力工作。')
     mach9 = make_q('除非说了有用，否则永远不要告诉任何人你做一件事的真实原因。')
     mach10 = make_q('只做有道义的事。')
     mach11 = make_q('如果不在这里或那里搞点小动作，想成功很难。')
     mach12 = make_q('所有人都有残暴的一面，遇到机会这一面就会冒出来。')
     mach13 = make_q('最烦跟其他人的最大的区别就是他太笨被抓到了。')
     mach14 = make_q('撒谎没有任何借口。')
     mach15 = make_q('绝大数人忘记去世父母容易，忘记亏钱难。')
     mach16 = make_q('绝对信任别人是自找麻烦。')
     mach17 = make_q('绝大多数人基本上是良善好人。')
     mach18 = make_q('对付别人最好的办法就是说他们想听的话。')
     mach19 = make_q('每分钟都有新的傻子出生。')
     mach20 = make_q('谦卑诚实比直达撒谎要好。')









class Survey(Page):
    form_model = 'player'
    form_fields = ['mach1', 'mach2', 'mach3', 'mach4', 'mach5', 'mach6', 'mach7', 'mach8'
        , 'mach9', 'mach10', 'mach11', 'mach12', 'mach13', 'mach14', 'mach15', 'mach16',
                   'mach17', 'mach18', 'mach19', 'mach20']



class End(Page):
    pass

page_sequence = [Survey, End]