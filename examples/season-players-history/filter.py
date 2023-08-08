import json

players = {}
with open('../data/players_by_number.json') as f:
  players = json.load(f)
  
for number in players['arsenal']:
  print(number['current']['name'], number['current']['since'])