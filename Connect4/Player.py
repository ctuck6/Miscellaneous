class Player:
	def __init__(self, name, piece):
		self.name = name
		self.piece = piece
		self.wins = 0

	def add_win(self):
		self.wins += 1

	def get_wins(self):
		return self.wins

	def get_name(self):
		return self.name

	def get_piece(self):
		return self.piece
