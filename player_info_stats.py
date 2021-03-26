from flask import Flask
from flask import render_template

import requests
import json

app = Flask(__name__)

def normalize_player_info(player_list: list, field_names: list, N: int = 10) -> list:
	"""Preps the data from disparate data sources to use a common schema"""
	players = []
	normalized_field_names = [
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

	# pluck the fields from the player list specified by the field_names
	try:
		for player_info in player_list:
			# filter out the data we don't need
			try:
				filtered_player_info = { key: player_info[key] for key in field_names }
			except KeyError:
				print('KeyError - normalize_player_info - missing key in player_info loop')
				return 'KeyError - normalize_player_info - missing key in player_info loop'
			except NameError:
				print('NameError - normalize_player_info - name error in player_info loop')
				return 'NameError - normalize_player_info - name error in player_info loop'

			# normalize the field names
			filtered_and_normalized_player_info = {}
			for k, v in filtered_player_info.items():
				normalized_field_name = normalized_field_names[field_names.index(k)]
				filtered_and_normalized_player_info[normalized_field_name] = v

			players.append(filtered_and_normalized_player_info)
	except NameError:
		print('NameError - player_list for loop')
		return 'NameError - player_list for loop'
	else:
		# return the first N players - if N < -1 then make it -1
		if N < -1:
			return players[:-1]
		else:
			return players[:N]

def get_stats_from_api(numrows: int = 10) -> list:
	"""Gets player info and stats from an api"""
	url = 'http://lookup-service-prod.mlb.com/json/named.search_player_all.bam?sport_code=%27mlb%27&active_sw=%27Y%27&name_part=%27a%25%27'
	try:
		response = requests.get(url).json()
	except json.decoder.JSONDecodeError:
		print('JSONDecodeError - get_stats_from_api - There was an error decoding the json from the response')
		return 'JSONDecodeError - get_stats_from_api - There was an error decoding the json from the response'

	fields_to_pluck = [
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

	try:
		normalized_player_info = normalize_player_info(response['search_player_all']['queryResults']['row'], fields_to_pluck, numrows)
	except KeyError:
		print('KeyError - get_stats_from_api - issue with key in normalize_player_info')
		return 'KeyError - get_stats_from_api - issue with key in normalize_player_info'
	except NameError:
		print('NameError - get_stats_from_api - issue with a name near normalize_player_info')
		return 'NameError - get_stats_from_api - issue with a name near normalize_player_info'

	return normalized_player_info

def get_stats_from_json(numrows: int = 10) -> list:
	"""Gets player info and stats from a json file"""
	try:
		f = open('mlbplayers.json',)
	except FileNotFoundError:
		print('FileNotFoundError - get_stats_from_json')
		return 'FileNotFoundError - get_stats_from_json'

	try:
		raw_player_data = json.load(f)
	except NameError:
		print('NameError - get_stats_from_json loading raw_player_data')
		return 'NameError - get_stats_from_json loading raw_player_data'

	fields_to_pluck = [
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

	try:
		normalized_player_info = normalize_player_info(raw_player_data['players'], fields_to_pluck, numrows)
	except KeyError:
		print('KeyError - get_stats_from_json - Invalid key in raw_player_data')
		return 'KeyError - get_stats_from_json - Invalid key in raw_player_data'
	except NameError:
		print('NameError - get_stats_from_json - something happened assigning normalized_player_info')
		return 'NameError - get_stats_from_json - something happened assigning normalized_player_info'
	else:
		return normalized_player_info

@app.route('/')
@app.route('/<numrows>/')
@app.route('/combined-stats/')
@app.route('/combined-stats/<numrows>/')
def get_combined_stats(numrows: str = '10'):
	api_stats = get_stats_from_api(int(numrows))
	json_stats = get_stats_from_json(int(numrows))

	try:
		rendered_template = render_template('player_list.html', data = (api_stats + json_stats))
	except NameError:
		print('NameError - get_combined_stats')
		return 'NameError - get_combined_stats'
	except TypeError:
		print('TypeError - get_combined_stats')
		return 'TypeError - get_combined_stats'
	except:
		print('Exception - get_combined_stats')
		return 'Exception - get_combined_stats'
	else:
		return rendered_template

@app.route('/api-stats/')
@app.route('/api-stats/<numrows>/')
def api_stats(numrows: str = '10'):
	print(numrows)
	try:
		rendered_template = render_template('player_list.html', data = get_stats_from_api(int(numrows)))
	except NameError:
		print('NameError - api_stats')
		return 'NameError - api_stats'
	except TypeError:
		print('TypeError - api_stats')
		return 'TypeError - api_stats'
	except:
		print('Exception - api_stats')
		return 'Exception - api_stats'
	else:
		return rendered_template

@app.route('/json-stats/')
@app.route('/json-stats/<numrows>/')
def json_stats(numrows: str = '10'):
	try:
		rendered_template = render_template('player_list.html', data = get_stats_from_json(int(numrows)))
	except NameError:
		print('NameError - json_stats')
		return 'NameError - json_stats'
	except TypeError:
		print('TypeError - json_stats')
		return 'TypeError - json_stats'
	except:
		print('Exception - json_stats')
		return 'Exception - json_stats'
	else:
		return rendered_template