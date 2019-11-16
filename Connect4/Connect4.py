class Connect4:
	def __init__(self, num_in_a_row=4):
		self.num_in_a_row = num_in_a_row
		self.num_of_moves = 0
		self.games_played = 0

	def reset(self):
		self.num_of_moves = 0

	def win(self, winner):
		if winner:
			print("Connect 4! Game Over!")
			print("{} wins!".format(winner.get_name()))
		else:
			print("Tie game! No one wins but hey, no one loses either!")

		print('\n')

	def show_score(self, player_list):
		print("{} wins: {}".format(player_list[0].get_name(), player_list[0].get_wins()))
		print("{} wins: {}".format(player_list[1].get_name(), player_list[1].get_wins()))
		print("Draws: {}".format(self.games_played - (player_list[0].get_wins() + player_list[1].get_wins())))
		print('\n')

	def play_again(self):
		newGame = input("Enter 'y' to play again, any other key to quit: ").lower()
		print('\n')

		if newGame == 'y':
			return True
		else:
			return False

	def check_for_winner(self, board, row, col, current_player):
		# checks vertical
		for i in range(row - (self.num_in_a_row - 1), row + self.num_in_a_row):
			if
			count = 0

			for j in range(self.num_in_a_row):
				if (i + j) >= 0 and (i + j) <= board.get_num_of_rows() - 1:
					if board.get_index(i + j, col) == current_player.get_piece():
						count += 1

						if count == self.num_in_a_row:
							return True
					else:
						count = 0

		# checks horizontal
		for i in range(col - (self.num_in_a_row - 1), col + self.num_in_a_row):
			count = 0

			for j in range(self.num_in_a_row):
				if (i + j) >= 0 and (i + j) <= board.get_num_of_cols() - 1:
					if board.get_index(row, i + j) == current_player.get_piece():
						count += 1

						if count == self.num_in_a_row:
							return True
					else:
						count = 0

		# checks diagonal going down and right


		# checks diagonal going down and left


	def player_move(self, board, current_player):
		empty = ' '
		column = int(input("{}, place your chip in a column. Enter '0' to quit the game: ".format(current_player.get_name()))) - 1
		print('\n')

		while column not in range(0, board.get_num_of_cols()) or board.get_index(0, column) != empty:
			if column == -1:
				quit()
			elif board.get_index(0, column) != empty:
				column = int(input("{}, that column is full. Try again, or enter '0' to quit the game: ".format(current_player.get_name())))
			else:
				print("That column is non-existent! Try again!")
				column = int(input("{}, place your chip in a column. Enter '0' to quit the game: ".format(current_player.get_name())))
				print('\n')

		for row in range(board.get_num_of_rows() - 1, -1, -1):
			if board.get_index(row, column) == empty:
				board.set_index(row, column, current_player.get_piece())
				break

		return [row, column]

	def increase_num_of_moves(self):
		self.num_of_moves += 1

	def get_num_of_moves(self):
		return self.num_of_moves

	def increase_games_played(self):
		self.games_played += 1
