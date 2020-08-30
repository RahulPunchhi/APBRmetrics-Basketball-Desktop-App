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
from datetime import datetime

today = datetime.today()
current_year_val = str(today.year)
prev_year_val = str(today.year - 1)

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

nba_team_data = []
nba_team_name = []
BaskRef_team_apbr_stats = 'https://www.basketball-reference.com/leagues/NBA_' + current_year_val + '.html'
page = urlopen(BaskRef_team_apbr_stats)
teamid = 0
soup = BeautifulSoup(page, 'html.parser')
teams_table_East = soup.find('table', attrs={'id': 'confs_standings_E'})
teams_table_West = soup.find('table', attrs={'id': 'confs_standings_W'})
teams_table_stats = soup.find('table', attrs={'id': 'team-stats-base'})

table_body_team_stats = teams_table_East.find_all('tr', attrs={'class': 'full_table'}) + teams_table_West.find_all('tr', attrs={'class': 'full_table'})
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

    # source for team colors - https://teamcolorcodes.com/nba-team-color-codes/

    colors_hashmap = {'MIL': '[0,.71,.27,1]',
                      'TOR': '[2.06,.17,.65,1]',
                      'PHI': '[0,1.07,1.82,1]',
                      'BOS': '[0,1.22,.51,1]',
                      'IND': '[0,.45,.98,1]',
                      'BRK': '[0,0,0,1]',
                      'ORL': '[0,1.25,1.97,1]',
                      'DET': '[2.00,.16,.46,1]',
                      'CHO': '[0,1.20,1.40,1]',
                      'MIA': '[1.52,0,.46,1]',
                      'WAS': '[0,.43,.92,1]',
                      'ATL': '[2.25,.68,.52,1]',
                      'CHI': '[2.06,.17,.65,1]',
                      'CLE': '[1.34,0,.56,1]',
                      'NYK': '[2.45,1.32,.38,1]',
                      'GSW': '[.29,.66,1.38,1]',
                      'DEN': '[.13,.34,.64,1]',
                      'POR': '[2.24,.58,.62,1]',
                      'HOU': '[2.06,.17,.65,1]',
                      'UTA': '[0,.43,.92,1]',
                      'OKC': '[0,1.25,1.95,1]',
                      'SAS': '[1.96,2.06,2.11,1]',
                      'LAC': '[.29,.66,1.48,1]',
                      'SAC': '[.91,.43,1.30,1]',
                      'LAL': '[.85,.37,1.30,1]',
                      'MIN': '[.12,.35,.64,1]',
                      'MEM': '[.093,1.18,1.69,1]',
                      'NOP': '[0,.022,.065,1]',
                      'DAL': '[0,.083,1.88,1]',
                      'PHO': '[.29,.17,.96,1]'
                    }

    nba_btn_str = ("\t\tButton:"
                   " \n\t\t\ttext: '%s'"
                   "\n\t\t\tbackground_color: %s"
                   "\n\t\t\ton_press: root.manager.current = '%s'\n") \
                  % (((nba_team_data[i])[7]), colors_hashmap[((nba_team_data[i])[7])], ((nba_team_data[i])[7]))

    # Image:\n\t\t\t\t source: 'Basketball_through_hoop.jpg'\n\t\t\t
    builderStringVal += nba_btn_str

for x in range(0, len(nba_team_name)):
    labels = 'Wins', 'Losses'
    fracs = [((nba_team_data[x])[0]), ((nba_team_data[x])[1])]

    plt.title((nba_team_data[x])[7] + " " + prev_year_val + "-" + current_year_val + " NBA Team Stats", color='white')
    plt.pie(fracs, labels=labels, shadow=True, autopct='%1.1f%%', textprops={'color': "w"})

    team_pie_name = 'team_win_loss_pie' + (nba_team_data[x])[7]
    plt.savefig(team_pie_name, transparent=True)
    plt.clf()
    builderStringVal += "<%s>:" \
                            "\n\tFloatLayout:" \
                                "\n\t\tLabel:" \
                                    "\n\t\t\tsize_hint: (.3, .35)" \
                                    "\n\t\t\tpos_hint: {'x':0, 'y':.65}" \
                                    "\n\t\t\ttext:'Simple Rating System (+/- Metric for Team Comparison):'" \
                                    "\n\t\t\thalign: 'center'" \
                                    "\n\t\t\tvalign: 'middle'" \
                                    "\n\t\t\ttext_size: self.size" \
                                "\n\t\tLabel:" \
                                    "\n\t\t\tsize_hint: (.3, .35)" \
                                    "\n\t\t\tpos_hint: {'x':0, 'y':.3}" \
                                    "\n\t\t\ttext:'%s'" \
                                "\n\t\tLabel:" \
                                    "\n\t\t\tsize_hint: (.7, .3)" \
                                    "\n\t\t\tpos_hint: {'x':0.3, 'y':0}" \
                                    "\n\t\t\ttext:'Points Per Game: %s'" \
                                    "\n\t\t\thalign: 'center'" \
                                    "\n\t\t\tvalign: 'middle'" \
                                    "\n\t\t\ttext_size: self.size" \
                                "\n\t\tImage:" \
                                    "\n\t\t\tsize_hint: (.7, .7)" \
                                    "\n\t\t\tpos_hint: {'x':.3, 'y':.3}" \
                                    "\n\t\t\tsource:'%s.png'" \
                                "\n\t\tButton:" \
                                    "\n\t\t\ttext: 'Back to all teams'" \
                                    "\n\t\t\tsize_hint: (.3, .3)" \
                                    "\n\t\t\tpos_hint: {'x':0.0, 'y':0.0}" \
                                    "\n\t\t\ton_press: root.manager.current = 'menu'\n" \
                        % (((nba_team_data[x])[7],
                            (nba_team_data[x])[6],
                            (nba_team_data[x])[4],
                            'team_win_loss_pie'+(nba_team_data[x])[7]))

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
