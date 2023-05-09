from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
  
  pass


class MyPage(Page):
   
   
   def vars_for_template(self):
     return dict(b=self.player.payoff)
  
  
   form_model ='player'
   form_fields = ['give1','give2','give3']



page_sequence = [Introduction,MyPage]
