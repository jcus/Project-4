
# Dependencies
from bs4 import BeautifulSoup
import requests
import os
import pandas as pd
import time
import sys



csv_path = "../data/player_add_info_errored_recs.csv"
bb_players_df = pd.read_csv(csv_path)
bb_players_df.head(10)

#start_row=2000
#end_row=10000

start_row=int(sys.argv[1])
end_row = int(sys.argv[2])

for i in range(start_row,end_row):
    print (i)

print("Startinng row",start_row, "Ending row", end_row) 

year=[]
team=[]
player_name = []
player_height = []
player_weight = []
player_position = []
process_status = []
for index, row in bb_players_df.iterrows():
    height=0
    weight=0
    position="NA"
#    print(index,"-" ,row['player_name'])
    if index < start_row:
        continue
    if index > end_row:
        break
    player = row['player_name'].lower().replace(".","").replace("'","").replace(",","").replace("`","")
    first_last = player.split()
    sports_ref_player =""
    for windex,word in enumerate(first_last):
        if windex==0 and len(first_last) > 1:
            sports_ref_player = word
        elif windex==0 and len(first_last) == 1:
            sports_ref_player = word + "-1"
        elif windex > 0 and len(first_last) > windex +1:
            sports_ref_player = sports_ref_player + "-" +   word
        elif windex > 0 and len(first_last) == windex+1:
            sports_ref_player = sports_ref_player + "-" +   word + "-1"
            
    print(sports_ref_player)
#    sports_ref_player = first_last[0] + "-" + first_last[1] + "-1"
    milliseconds = 100
    seconds = 0.001 * milliseconds
    start_time = time.time()
    time.sleep(seconds)
    stop_time = time.time()
#    time.sleep(1)
    player_name.append(row['player_name'])
    year.append(row['year'])
    team.append(row['team'])
    url = 'https://www.sports-reference.com/cbb/players/' + sports_ref_player+'.html'
    try:
        response = requests.get(url)
        if response.text.find("Position:") > -1 and response.text.find('itemprop="height"') > -1 :
            print("Found url")
        else :
            response = requests.get(url.replace("-1","-2"))
            
        soup = BeautifulSoup(response.text, 'html.parser')
        if response.text.find("Position:") > -1 and response.text.find('itemprop="height"') > -1 : 
            results = soup.find_all('div', id='info')
            #print(results[0])
            ptags = results[0].find_all('p')
#            print(ptags[0].contents[2].strip())
            position=ptags[0].contents[2].strip()
            print('Height tags',ptags[0].contents[3].contents[-1].strip())
            print(ptags[0].contents[3].contents[-1].strip())
            poop = ptags[0].contents[3].contents[-1].strip().replace("(","").replace(")","").replace("cm","").replace("kg","")
            print(poop)
            height_weight= poop.split(",\xa0")
            if len(height_weight) > 1 :
                height=height_weight[0]
                weight=height_weight[1]
            elif len(height_weight) > 0 :
                height=height_weight[0]
            else:
                height=-200
                weight=-200
            
#            height,weight = poop.split(",\xa0")
            print(height,"-" ,weight)
            player_position.append(position)
#            print('appended position:',len(player_position))
            player_height.append(height)
            player_weight.append(weight)
#            print('appended weight:',len(player_weight))
            process_status.append("Success")
        else:
            print("Not Found in :",response.text)
            process_status.append("Failure: Did not find player")
            player_position.append(-1)
            player_height.append(-1)
            player_weight.append(-1)
    except:
            (type, value, tb) = sys.exc_info()
            err = "%s" % value
            process_status.append("Failure: Other Error")
            print("Other Error")
            player_position.append(-100)
            player_height.append(-100)
            player_weight.append(-100)
#    print(len(player_name),len(player_position),len(player_height),len(process_status))
    if len(player_name) != len(player_position):
        break;
import numpy as np
player_add_info_dict = {"player_name":player_name,"year":year,"team":team,"player_position":player_position,"player_height":player_height,"player_weight":player_weight,"process_status":process_status}
player_add_info_df=pd.DataFrame(data=player_add_info_dict)
#process_status

#player_add_info_df["process_status"] = np.where(player_add_info_df["process_status"] == "Success", "Success", "Failure")
player_add_info_df.head()

player_file = "player_add_info_retry"+str(start_row)+"_"+str(end_row)+".csv"
print(player_file)
player_add_info_df.to_csv(player_file)
