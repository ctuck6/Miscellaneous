from Card import Card

class Board:
	def __init__(self, size=4):
		self.size = size
		self.board = self.initialize_board(size)

	def initialize_board(self, size):
		import random
		from random import shuffle

		array = list()
		num_of_unique_cards = (self.size ** 2) // 2
		nums_1 = random.sample(range(1, num_of_unique_cards + 1), num_of_unique_cards)
		nums_2 = random.sample(range(1, num_of_unique_cards + 1), num_of_unique_cards)
		nums_array = nums_1 + nums_2
		shuffle(nums_array)
		count = 0

		for i in range(self.size):
			array.append(list())

			for j in range(self.size):
				array[i].append(Card(nums_array[count]))
				count += 1

		return array

	def get_card(self, x, y):
		return self.board[y][x].get_value()

	def flip_pair(self, card_1_x, card_1_y, card_2_x, card_2_y):
		showing = True
		hidden = False

		if self.board[card_1_y][card_1_x].get_status():
			self.board[card_1_y][card_1_x].set_status(hidden)
			self.board[card_2_y][card_2_x].set_status(hidden)
		else:
			self.board[card_1_y][card_1_x].set_status(showing)
			self.board[card_2_y][card_2_x].set_status(showing)

	def show_board(self, card_1_x=None, card_1_y=None, card_2_x=None, card_2_y=None):
		print('\n')
		print(('----' * self.size) + '-----')
		print('|   ', end='')

		for i in range(self.size):
			print('| {} '.format(str(i)), end='')

		print('|')

		for i in range(self.size):
			print(('----' * self.size) + '-----')
			print('| {} '.format(i), end='')

			for j in range(self.size):
				if self.board[i][j].get_status():
					if card_1_x != None:
						print('| {} '.format(self.board[i][j].get_value()), end='')
					else:
						print('|   ', end='')
				else:
					print('| X ', end='')

			print('|')

		print(('----' * self.size) + '-----')
