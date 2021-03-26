from flask import Flask
from flask import jsonify

import requests
import json

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'

@app.route('/combined-stats')
def get_combined_stats():
	api_stats = get_stats_from_api()
	print(api_stats)
	json_stats = get_stats_from_json()
	print(json_stats)

	return jsonify(api_stats + json_stats)

def normalize_player_info(player_list, field_names, N=10):
	players = []
	fieldNames = [
		'position',
		'weight',
		'heightInches',
		'bats',
		'nameFirst',
		'heightFeet',
		'fullTeamName',
		'throws',
		'nameLast'
	]

	for playerInfo in player_list:
		filteredPlayerInfo = { key: playerInfo[key] for key in field_names }

		# normalize the field names
		filteredAndNormalizedPlayerInfo = {}
		for k, v in filteredPlayerInfo.items():
			normalizedFieldName = fieldNames[field_names.index(k)]
			filteredAndNormalizedPlayerInfo[normalizedFieldName] = v

		players.append(filteredAndNormalizedPlayerInfo)

	return players[:N]

def get_stats_from_api():
	url = "http://lookup-service-prod.mlb.com/json/named.search_player_all.bam?sport_code=%27mlb%27&active_sw=%27Y%27&name_part=%27a%25%27"
	response = requests.get(url).json()

	fieldsToPluck = [
		'position',
		'weight',
		'height_inches',
		'bats',
		'name_first',
		'height_feet',
		'team_full',
		'throws',
		'name_last'
	]

	return normalize_player_info(response['search_player_all']['queryResults']['row'], fieldsToPluck, 10)

def get_stats_from_json():
	f = open("mlbplayers.json",)
	rawPlayerData = json.load(f)

	fieldsToPluck = [
		'position',
		'weightLbs',
		'heightIn',
		'bats',
		'firstName',
		'heightFt',
		'teamName',
		'throws',
		'lastName'
	]

	return normalize_player_info(rawPlayerData['players'], fieldsToPluck, 10)

@app.route('/api-stats')
def api_stats():
	return jsonify(get_stats_from_api())

@app.route('/json-stats')
def json_stats():
	return jsonify(get_stats_from_json())