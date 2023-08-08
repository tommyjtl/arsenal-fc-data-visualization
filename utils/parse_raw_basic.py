from bs4 import BeautifulSoup
import requests
import json
from unidecode import unidecode

# Define a function to convert the BeautifulSoup tree to a JSON format
def soup_to_json(element):
    if isinstance(element, str):
        return element
    else:
        data = {}
        if element.name:
            data["tag"] = element.name
        if element.attrs:
            data["attrs"] = element.attrs
        data["children"] = [soup_to_json(child) for child in element.contents if child != '\n']
        return data

# url = "https://www.transfermarkt.us/fc-arsenal/rueckennummern/verein/11"
# html_content = requests.get(url).text
html_content = open("../raw/raw.html", "r").read()
soup = BeautifulSoup(html_content, "html.parser")
table = soup.find('table')
trs = table.find_all('tr', attrs={'class': 'filter-row'})

# # ignore non-current players for now
# additional_trs = table.find_all('tr', attrs={'class': 'bg_grey'})
# # concate trs and additional_trs
# trs = trs + additional_trs

players = {
  'arsenal': []
}

# count = 0
for tr in trs:
  number = tr.find('td', attrs={'class': 'zentriert'}).text
  print(number)
  
  current = {
    'avatar': '',
    'name': '',
    'since': '',
  }
  
  # current player  
  current_player_html = tr.find('table', attrs={'class': 'inline-table'})
  current['avatar'] = current_player_html.find('img', attrs={'class': 'bilderrahmen-fixed'}).get('src')
  # current['name'] = unidecode(current_player_html.find('img', attrs={'class': 'bilderrahmen-fixed'}).get('title'))
  current['name'] = current_player_html.find('img', attrs={'class': 'bilderrahmen-fixed'}).get('title')
  current['since'] = current_player_html.find_all('td')[-1].text.replace('since', '').replace(' ', '')
  
  # history players
  history = []
  history_players_html = tr.find('div', attrs={'style': 'padding-left: 6px;padding-top: 3px; line-height:1.6; padding-right: 6px'})
  history_players_dict = soup_to_json(history_players_html)
  # print(history_players_dict['children'])
  hpd_children = history_players_dict['children']
  for i in range(0, len(hpd_children), 2):
    # if item is a dict
    player = {
      'name': '',
      'position': '',
      'period': '',
    }
    
    print(json.dumps(hpd_children[i], indent=2))
    print(hpd_children[i + 1])
    
    if len(hpd_children[i]['children']) >= 2:
      # player['name'] = unidecode(hpd_children[i]['children'][0]['children'][0])
      player['name'] = hpd_children[i]['children'][0]['children'][0]
      player['position'] = hpd_children[i]['children'][1]['attrs']['title']
      player['period'] = hpd_children[i + 1].strip().replace(',', '')
    elif len(hpd_children[i]['children']) == 1:
      # player['name'] = unidecode(hpd_children[i]['children'][0]['children'][0])
      player['name'] = hpd_children[i]['children'][0]['children'][0]
      player['period'] = hpd_children[i + 1].strip().replace(',', '')
      
    
    history.append(player)
  
  players['arsenal'].append({
    'number': int(number),
    'current': current,
    'history': history
  })
  
  # count += 1
  # if (count == 1):
  #   break
  
player_json = json.dumps(players, indent=2)
# print(player_json)

# store json to the file
with open('../data/players_by_number.json', 'w') as outfile:
  outfile.write(player_json)
  