import json

players = {}
# load `players.json`
with open('./data/players_by_number.json') as f:
  players = json.load(f)
  
print('Current total players:\t', len(players['arsenal']))
print('---')
print('Number\t Since\t Name')
for player in players['arsenal']:
  if player['current']['name'] != '':
    print(player['number'], '\t',  
          player['current']['since'], '\t',
          player['current']['name'],
          # player['current']['avatar']
    )
