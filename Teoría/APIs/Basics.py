import pandas as pd
import matplotlib.pyplot as plt

dict_={'a':[11,21,31],'b':[12,22,32]}

df=pd.DataFrame(dict_)
type(df)

df.head()

df.mean()

!pip install nba_api

from nba_api.stats.static import teams
import matplotlib.pyplot as plt

def one_dict(list_dict):
    keys=list_dict[0].keys()
    out_dict={key:[] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict

nba_teams = teams.get_teams()

nba_teams[0:3]

#Convert dictionarie on a table

dict_nba_team=one_dict(nba_teams)
df_teams=pd.DataFrame(dict_nba_team)
df_teams.head()

df_warriors=df_teams[df_teams['nickname']=='Warriors']
df_warriors

id_warriors=df_warriors[['id']].values[0][0]
# we now have an integer that can be used to request the Warriors information 
id_warriors

from nba_api.stats.endpoints import leaguegamefinder

#CALCULATE THE MEAN
# Write your code below and press Shift+Enter to execute
games_home['PTS'].mean()
games_away['PTS'].mean()
