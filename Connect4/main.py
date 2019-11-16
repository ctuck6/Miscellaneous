from Board import Board
from Connect4 import Connect4
from Player import Player

def main():
	print("Welcome to connect 4!")

	p1_name = input("Player 1, enter your name: ")
	p2_name = input("Player 2, enter your name: ")
	player_one = Player(p1_name, "R")
	player_two = Player(p2_name, "Y")
	board = Board(6, 7)
	game = Connect4()
	player_list = [player_one, player_two]

	game_over = False
	play_again = True
	winner = False

	print("\nGame in progress! Good luck, may the odds be with you both!\n")

	while play_again:
		board.display_grid()

		while not game_over:
			coordinates = game.player_move(board, player_list[0])
			board.display_grid()
			game.increase_num_of_moves()
			game_over = game.check_for_winner(board, coordinates[0], coordinates[1], player_list[0])

			if not game_over:
				player_list[0], player_list[1] = player_list[1], player_list[0]

		if game.get_num_of_moves() < (board.get_num_of_rows() * board.get_num_of_cols()):
			winner = player_list[0]
			winner.add_win()
			game.increase_games_played()
			game.win(winner)
			board.display_grid(True)
			game.show_score(player_list)
			play_again = game.play_again()

			if play_again:
				game.reset()
				board.reset()
				game_over = False
				winner = False

if __name__ == "__main__":
	main()
