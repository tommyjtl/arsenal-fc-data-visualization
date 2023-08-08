# Arsenal FC Data Visualization

Some structured dataset and data visualizations for Arsenal FC. <a>#COYG</a>

```shell
.
├── raw # raw data 
│   ├── raw.html
│   └── raw_player_example.html
├── data # proccessed structured data
│   └── players_by_number.json
├── examples # examples of visualizations
│   ├── season-players-history
│   └── squad-number-history
└── utils # scripts to parse raw data
    └── parse_raw.py
```

## Preview

Run the `preview.py` to load the current players playing for Arsenal FC. Example output is shown below.

```bash
$ python3 preview.py 
Current total players:   32
---
Number   Since   Name
1        22/23   Aaron Ramsdale
2        23/24   William Saliba
3        19/20   Kieran Tierney
4        21/22   Ben White
5        21/22   Thomas Partey
6        20/21   Gabriel Magalhães
7        20/21   Bukayo Saka
8        21/22   Martin Ødegaard
9        22/23   Gabriel Jesus
10       21/22   Emile Smith Rowe
11       21/22   Gabriel Martinelli
12       23/24   Jurrien Timber
13       23/24   Rúnar Alex Rúnarsson
14       21/22   Eddie Nketiah
15       22/23   Jakub Kiwior
16       16/17   Rob Holding
17       19/20   Cédric Soares
18       21/22   Takehiro Tomiyasu
19       22/23   Leandro Trossard
20       22/23   Jorginho
21       22/23   Fábio Vieira
23       21/22   Albert Sambi Lokonga
24       19/20   Reiss Nelson
25       20/21   Mohamed Elneny
26       23/24   Folarin Balogun
27       22/23   Marquinhos
29       23/24   Kai Havertz
30       22/23   Matt Turner
31       22/23   Karl Hein
33       23/24   Arthur Okonkwo
35       22/23   Oleksandr Zinchenko
41       23/24   Declan Rice
```

## Data

### Players by number

As appeared in the `./data/players_by_number.json` file, this file contains the data of all squad numbers used with their corresponding player name. Each indice in the `arsenal` has the structure of:

```json
{
  "number": 1,
  "current": {
    "avatar": "https://img.a.transfermarkt.technology/portrait/medium/427568-1681828000.jpg?lm=1",
    "name": "Aaron Ramsdale",
    "since": "22/23"
  },
  "history": [
    {
      "name": "Bernd Leno",
      "position": "Goalkeepers",
      "period": "(19/20 - 21/22)"
    }
  ]
}
```

### Players by season

As appeared in the `./data/players_by_season.json` file, this file contains how many seasons a player has played. Each key is the name of the player, and each player has the following data structure:

```json
{
  "Thierry Henry": [
    "11/12",
    "99/00",
    "00/01",
    "01/02",
    "02/03",
    "03/04",
    "04/05",
    "05/06",
    "06/07"
  ]
}
```

## Acknowledgements

- All data in this repository is scraped from the internet, sources used are located in [sources.md](./raw/source.md).