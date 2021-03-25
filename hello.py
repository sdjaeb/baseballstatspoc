from flask import Flask
from flask import request

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
	return 'Stats from API'

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
	players = json.load(f)

	return players