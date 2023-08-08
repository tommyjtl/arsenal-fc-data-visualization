import json
import csv

players = {}
data = []

# load `players.json`
with open('../data/players_by_number.json') as f:
  players = json.load(f)

for player in players['arsenal']:
  # print(player['number'], '\t',  
  #       player['current']['since'], '\t',
  #       player['current']['name'],
  # )
  data.append([
    'Number ' + str(player['number']), 
    player['current']['name'],
    player['current']['since'].split('/')[-1]
  ])
  for history in player['history']:
    data.append([
      'Number ' + str(player['number']), 
      history['name'], 
      # history['period']
      history['period'].replace(' ', '').replace('(', '').replace(')', '').split('-')[-1].split('/')[-1]
    ])
    # print(history['period'].replace(' ', '').replace('(', '').replace(')', '').split('-')[-1].split('/')[-1])
  # break

# for d in data:
#   print(d)
  
with open('sankey.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['Number', 'Player', 'Last Season'])
  for row in data:
      writer.writerow(row)

print("CSV file created successfully.")