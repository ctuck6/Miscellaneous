class Card:
	def __init__(self, value):
		self.value = value
		self.flipped = False

	def get_value(self):
		return self.value

	def get_status(self):
		return self.flipped

	def set_status(self, status):
		self.flipped = status
