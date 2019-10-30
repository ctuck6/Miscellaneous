class Player:
	def __init__(self, name):
		self.wins = 0
		self.name = name

	def add_win(self):
		self.wins += 1

	def get_wins(self):
		return self.wins

	def get_name(self):
		return self.name
