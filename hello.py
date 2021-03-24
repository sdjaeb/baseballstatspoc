from flask import Flask
from flask import request

app = Flask(__name__)

''' http://lookup-service-prod.mlb.com/json/named.search_player_all.bam?sport_code=%27mlb%27&active_sw=%27Y%27&name_part=%27pu%25%27
'''
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/stats')
def get_stats():
	return 'Stats!'