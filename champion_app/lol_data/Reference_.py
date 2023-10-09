import requests

url = "http://ddragon.leagueoflegends.com/cdn/13.19.1/data/fr_FR/champion.json"
req = requests.get(url)
res = req.json()
data = res.get('data')
champ_list = list(data)

url_ = 'http://ddragon.leagueoflegends.com/cdn/{}/data/fr_FR/champion/{}.json'

version = '13.18.1'
format_ = res.get('format')