from tkinter import *
from urllib.request import urlopen
from bs4 import BeautifulSoup
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import *
from kivy.uix.button import *
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from pylab import figure, axes, pie, title, show
import matplotlib.pyplot as plt
from kivy.core.image import Image as CoreImage

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

nba_team_data = []
nba_team_name = []
BaskRef_team_apbr_stats = 'https://www.basketball-reference.com/leagues/NBA_2018.html'
page = urlopen(BaskRef_team_apbr_stats)
teamid = 0
soup = BeautifulSoup(page, 'html.parser')
teams_table_East = soup.find('table', attrs={'id': 'confs_standings_E'})
teams_table_West = soup.find('table', attrs={'id': 'confs_standings_W'})
teams_table_stats = soup.find('table', attrs={'id': 'team-stats-base'})

table_body_team_stats = teams_table_East.find_all('tr', attrs={'class': 'full_table'})+teams_table_West.find_all('tr', attrs={'class': 'full_table'})
table_body_team_name = teams_table_East.find_all('a')+teams_table_West.find_all('a')


for row in table_body_team_stats:
   col_val = row.find_all('td')
   col_val = [ele.text.strip() for ele in col_val]
   nba_team_data.append([ele for ele in col_val if ele])

for row in table_body_team_name:
    hrefTeamVal = row['href']
    hrefTeamVal = hrefTeamVal.split('/')[2]
    nba_team_name.append(hrefTeamVal)

full_nba_team_list = nba_team_data

for x in range(0, len(nba_team_name)):
    nba_team_data[x].append(nba_team_name[x])
    nba_team_data[x].append(teamid)
    teamid += 1

builderStringVal = """<MenuScreen>:
    GridLayout:
        cols: 5\n"""

for i in range(0, len(nba_team_name)):
    builderStringVal += ("\t\tButton: \n\t\t\ttext: '%s' \n\t\t\ton_press: root.manager.current = '%s'\n") % (((nba_team_data[i])[7]), ((nba_team_data[i])[7]))

for x in range(0, len(nba_team_name)):
    labels = 'Wins', 'Losses'
    fracs = [((nba_team_data[x])[0]), ((nba_team_data[x])[1])]

    plt.title((nba_team_data[x])[7] + " 2017-2018 NBA Team Stats")
    plt.pie(fracs, labels=labels, shadow=True, autopct='%1.1f%%')
    team_pie_name = 'team_win_loss_pie'+(nba_team_data[x])[7]
    plt.savefig(team_pie_name)
    plt.clf()
    builderStringVal += "<%s>:\n\tFloatLayout:\n\t\tLabel:\n\t\t\tsize_hint: (.3, .35)\n\t\t\tpos_hint: {'x':0, 'y':.65}\n\t\t\ttext:'Simple Rating System (+/- Metric for Team Comparison):'\n\t\t\thalign: 'center'\n\t\t\tvalign: 'middle'\n\t\t\ttext_size: self.size\n\t\tLabel:\n\t\t\tsize_hint: (.3, .35)\n\t\t\tpos_hint: {'x':0, 'y':.3}\n\t\t\ttext:'%s'\n\t\tLabel:\n\t\t\tsize_hint: (.7, .3)\n\t\t\tpos_hint: {'x':0.3, 'y':0}\n\t\t\ttext:'Points Per Game: %s'\n\t\t\thalign: 'center'\n\t\t\tvalign: 'middle'\n\t\t\ttext_size: self.size\n\t\tImage:\n\t\t\tsize_hint: (.7, .7)\n\t\t\tpos_hint: {'x':.3, 'y':.3}\n\t\t\tsource:'%s.png'\n\t\tButton:\n\t\t\ttext: 'Back to all teams'\n\t\t\tsize_hint: (.3, .3)\n\t\t\tpos_hint: {'x':0.0, 'y':0.0}\n\t\t\ton_press: root.manager.current = 'menu'\n" % (((nba_team_data[x])[7], (nba_team_data[x])[6], (nba_team_data[x])[4], 'team_win_loss_pie'+(nba_team_data[x])[7]))

Builder.load_string(builderStringVal)

# Declare all screens
class MenuScreen(Screen):
    pass

class TOR(Screen):
    pass

class BOS(Screen):
    pass

class CLE(Screen):
    pass

class IND(Screen):
    pass

class WAS(Screen):
    pass

class PHI(Screen):
    pass

class MIA(Screen):
    pass

class MIL(Screen):
    pass

class DET(Screen):
    pass

class CHO(Screen):
    pass

class NYK(Screen):
    pass

class CHI(Screen):
    pass

class BRK(Screen):
    pass

class ATL(Screen):
    pass

class ORL(Screen):
    pass

class HOU(Screen):
    pass

class GSW(Screen):
    pass

class POR(Screen):
    pass

class NOP(Screen):
    pass

class OKC(Screen):
    pass

class MIN(Screen):
    pass

class SAS(Screen):
    pass

class LAC(Screen):
    pass

class UTA(Screen):
    pass

class DEN(Screen):
    pass

class LAL(Screen):
    pass

class SAC(Screen):
    pass

class DAL(Screen):
    pass

class PHO(Screen):
    pass

class MEM(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(TOR(name='TOR'))
sm.add_widget(BOS(name='BOS'))
sm.add_widget(CLE(name='CLE'))
sm.add_widget(IND(name='IND'))
sm.add_widget(WAS(name='WAS'))
sm.add_widget(PHI(name='PHI'))
sm.add_widget(MIA(name='MIA'))
sm.add_widget(MIL(name='MIL'))
sm.add_widget(DET(name='DET'))
sm.add_widget(CHO(name='CHO'))
sm.add_widget(NYK(name='NYK'))
sm.add_widget(CHI(name='CHI'))
sm.add_widget(BRK(name='BRK'))
sm.add_widget(ATL(name='ATL'))
sm.add_widget(ORL(name='ORL'))
sm.add_widget(HOU(name='HOU'))
sm.add_widget(GSW(name='GSW'))
sm.add_widget(POR(name='POR'))
sm.add_widget(NOP(name='NOP'))
sm.add_widget(OKC(name='OKC'))
sm.add_widget(MIN(name='MIN'))
sm.add_widget(SAS(name='SAS'))
sm.add_widget(LAC(name='LAC'))
sm.add_widget(UTA(name='UTA'))
sm.add_widget(DEN(name='DEN'))
sm.add_widget(LAL(name='LAL'))
sm.add_widget(SAC(name='SAC'))
sm.add_widget(DAL(name='DAL'))
sm.add_widget(PHO(name='PHO'))
sm.add_widget(MEM(name='MEM'))

class TestApp(App):
    def build(self):
        self.title = 'APBRmetrics Basketball Desktop App'
        return sm

if __name__ == '__main__':
    TestApp().run()
