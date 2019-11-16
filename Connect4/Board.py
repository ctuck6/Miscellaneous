class Board:
	def __init__(self, rows, cols):
		self.rows = rows
		self.cols = cols
		self.board = [[' ' for column in range(cols)] for row in range(rows)]

	def reset(self):
		self.board = [[' ' for column in range(self.cols)] for row in range(self.rows)]

	def get_num_of_rows(self):
		return self.rows

	def get_num_of_cols(self):
		return self.cols

	def get_index(self, row, col):
		return self.board[row][col]

	def set_index(self, row, col, value):
		self.board[row][col] = value

	def display_grid(self, winner=False):
		if not winner:
			for num in range(self.cols):
				print(' ', end="")
				print("  " + str(num + 1) + "  ", end="")

			print(' ')

		boarder = ""

		for num in range(self.cols):
			boarder += "------"

		boarder += '-'
		print(boarder)

		for row in range(self.rows):
			for col in range(self.cols):
				print("¦  {}  ".format(self.board[row][col]), end="")

			print("¦\n" + boarder)

		print('\n')
