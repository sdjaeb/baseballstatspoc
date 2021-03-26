class Player:
	def __init__(self, player_data):
		self.data = player_data

	def get(self, field):
		return self.data[field]

	def set(self, field, value):
		self.data[field] = value

	def __str__(self):
		player_details = ''
		for key, value in self.data.items():
			player_details += key + ': ' + value + '\n'

		return player_details