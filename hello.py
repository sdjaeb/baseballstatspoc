from flask import Flask
from flask import jsonify

import requests
import httpx
import json

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

'''
	Eventually pass in filter (partial name, positions, team, etc)
'''
@app.route('/api-stats')
def get_stats_from_api():
	'''
		http://lookup-service-prod.mlb.com/json/named.search_player_all.bam?sport_code=%27mlb%27&active_sw=%27Y%27&name_part=%27pu%25%27
		Only return:
			full name,
			full team name,
			player id,
			weight,
			height (ft' in"),
			bats/throws,
			position
	'''
	url = "http://lookup-service-prod.mlb.com/json/named.search_player_all.bam?sport_code=%27mlb%27&active_sw=%27Y%27&name_part=%27a%25%27"
	response = requests.get(url).json()

	normalizedFields = [ 'position', 'weight', 'height_inches', 'bats', 'name_first', 'height_feet', 'team_full', 'throws', 'name_last' ]

	# Extract the necessary data
	# Iterate over the response object
	players = []
	for playerInfo in response['search_player_all']['queryResults']['row']:
		filteredPlayerInfo = { normalizedKey: playerInfo[normalizedKey] for normalizedKey in normalizedFields }
		players.append(filteredPlayerInfo)

	return jsonify(players[:10])

@app.route('/json-stats')
def get_stats_from_json():
	'''
		Load player_stats.json
		Only return:
			full name,
			full team name,
			player id,
			weight,
			height (ft' in"),
			bats/throws,
			position
	'''
	f = open("mlbplayers.json",)
	rawPlayerData = json.load(f)

	normalizedFields = [ 'position', 'weightLbs', 'heightIn', 'bats', 'firstName', 'heightFt', 'teamName', 'throws', 'lastName' ]

	# Extract the necessary data
	# Iterate over the response object
	players = []
	for playerInfo in rawPlayerData['players']:
		filteredPlayerInfo = { normalizedKey: playerInfo[normalizedKey] for normalizedKey in normalizedFields }
		players.append(filteredPlayerInfo)

	return jsonify(players[:10])