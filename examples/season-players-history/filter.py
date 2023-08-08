import json

players = {}
raw_players = {}
as_of_now = '23/24'

with open('../../data/players_by_number.json') as f:
  raw_players = json.load(f)
  
for number in raw_players['arsenal']:
  periods = [number['current']['since'], as_of_now]
  
  if number['current']['name'] not in players:
    # print(number['number'], number['current']['name'], periods)
    players[number['current']['name']] = []
    players[number['current']['name']].append(
      {
        'number': number['number'],
        'periods': periods
      }
    )
  elif number['current']['name'] in players:
    # print(number['number'], number['current']['name'], periods)
    players[number['current']['name']].append(
      {
        'number': number['number'],
        'periods': periods
      }
    )
  
  for h in number['history']:
    # print(h)
    periods = h['period'].replace(' ', '').replace('(', '').replace(')', '').split('-')
    
    if h['name'] not in players:
      # print(number['number'], h['name'], periods)
      players[h['name']] = []
      players[h['name']].append({
        'number': number['number'],
        'periods': periods
      })
    elif h['name'] in players:
      # print(number['number'], h['name'], periods)
      players[h['name']].append({
        'number': number['number'],
        'periods': periods
      })
  
print('total players:', len(players))
  
# save players to file
with open('output.json', 'w') as f:
  json.dump(players, f, indent=2)
  