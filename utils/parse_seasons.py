import json

players = {}
raw_players = {}
as_of_now = '23/24'

def extract_seasons(start, end):
  '''
  This function takes two strings as input:
    - start: a string representing the start of a season, example: '18/19'
    - end: a string representing the end of a season, example: '22/23'
  
  This function returns a list of seasons starting from the start season and ending with the end season.
  
  Edges cases:
    - if start and end are the same, return a list with one element: start
    - if the start season is '99/00', and the end season is starting from '00/01', return a list with all the seasons from '99/00' to the end season, for example:
      - extract_seasons('99/00', '03/04') returns ['99/00', '00/01', '01/02', '02/03', '03/04']
      - extract_seasons('99/00', '00/01') returns ['99/00', '00/01']
    
  Example: extract_seasons('18/19', '22/23') returns ['18/19', '19/20', '20/21', '21/22', '22/23']
  '''
  if start == end:
    return [start]
  
  start_year = int(start.split('/')[0])
  end_year = int(end.split('/')[0])
  seasons = []
  
  for year in range(start_year, end_year + 1):
    # append 0 to the year if the string is only one character long
    seasons.append(('0' + str(year) if len(str(year)) == 1 else str(year)) + 
                   '/' + 
                   ('0' + str(year + 1)[-2:] if len(str(year + 1)[-2:]) == 1 else str(year + 1)[-2:])
    )
  
  if end_year < start_year:
    for year in range(start_year, 100):
      seasons.append(
        ('0' + str(year) if len(str(year)) == 1 else str(year)) + 
        '/' + 
        ('0' + str(year + 1)[-2:] if len(str(year + 1)[-2:]) == 1 else str(year + 1)[-2:])
      )
    for year in range(0, end_year + 1):
      seasons.append(
        ('0' + str(year) if len(str(year)) == 1 else str(year)) + 
        '/' + 
        ('0' + str(year + 1)[-2:] if len(str(year + 1)[-2:]) == 1 else str(year + 1)[-2:])
      )

  return seasons

with open('../data/players_by_number.json') as f:
  raw_players = json.load(f)
  
for number in raw_players['arsenal']:
  if number['current']['since'] != '':
    periods = [number['current']['since'], as_of_now]
    # print(number['current']['name'], periods)
  
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
    if len(periods) == 1:
      periods.append(periods[0])
    
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
# print(json.dumps(players, indent=2))

players_output = {}

for player in players.keys():
  # print(player, players[player])
  # print(player, end = ' ')
  periods = []
  for i in players[player]:
    # print(player, i['periods'])
    periods += extract_seasons(
      i['periods'][0], 
      i['periods'][1]
    )
    
  players_output[player] = periods
  
longest_season_played = {
  'name': '',
  'seasons': 0
}
for i in players_output.keys():
  if longest_season_played['seasons'] < len(players_output[i]):
    longest_season_played['name'] = i
    longest_season_played['seasons'] = len(players_output[i])

print('longest season played:', longest_season_played)

# save players to file
with open('../data/players_by_season.json', 'w') as f:
  json.dump(players_output, f, indent=2)
  
players_seasons = {}
with open('../data/players_by_season.json') as f:
  players_seasons = json.load(f)
  
