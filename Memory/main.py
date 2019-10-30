from Player import Player
from Board import Board

def main():
	import time, os

	print('Welcome to memory! Enter your name and press enter to play!')
	player_name = input("If you would like to quit, enter '0' and press enter: ")

	if player_name == '0':
		return

	BOARD_SIZE = 4
	player = Player(player_name)
	board = Board(BOARD_SIZE)
	game_over = False

	while not game_over:
		winner = False
		cards_correct = 0

		while not winner:
			os.system('cls' if os.name == 'nt' else 'clear')
			board.show_board()

			print('\nEnter the X-coordinate of the first card you would like to flip, followed by the Y-coordinate.')
			card_1 = input('(Example: 00 would be choosing the top left card): ')

			while (len(card_1) > 2 or len(card_1) < 1) \
			or (card_1[0] < '0' or card_1[0] > str(BOARD_SIZE)) \
			or (card_1[1] < '0' or card_1[1] > str(BOARD_SIZE)):
				card_1 = input('Oops! Choose a valid card: ')

			print('\nEnter the X-coordinate of the second card you would like to flip, followed by the Y-coordinate.')
			card_2 = input('(Example: 00 would be choosing the top left card): ')

			while (len(card_2) > 2 or len(card_2) < 1) \
			or (card_2[0] < '0' or card_2[0] > str(BOARD_SIZE)) \
			or (card_2[1] < '0' or card_2[1] > str(BOARD_SIZE)):
				card_2 = input('Oops! Choose a valid card: ')

			card_1_x = int(card_1[0])
			card_1_y = int(card_1[1])
			card_2_x = int(card_2[0])
			card_2_y = int(card_2[1])

			board.flip_pair(card_1_x, card_1_y, card_2_x, card_2_y)
			board.show_board(card_1_x, card_1_y, card_2_x, card_2_y)

			if board.get_card(card_1_x, card_1_y) == board.get_card(card_2_x, card_2_y):
				print('\nNice! You found a match! Keep going!')
				cards_correct += 1
			else:
				print('\nOh no, those cards to do match! Try to remember what these two cards are for the future!')
				board.flip_pair(card_1_x, card_1_y, card_2_x, card_2_y)

			if cards_correct >= ((BOARD_SIZE ** 2) // 2):
				winner = True
				player.add_win()
			else:
				print('Waiting 5 seconds to let you study the cards...')
				time.sleep(5)

		board.show_board()
		play_again = input("\nYou win! Wow, you're good at this! You have won {} game(s)!".format(player.get_wins()))
		play_again = input('Would you like to play again (y/n): ')

		if play_again.lower() == 'n':
			game_over = True
		elif play_again.lower() == 'y':
			pass
		else:
			while play_again.lower() != 'y' and play_again.lower() != 'n':
				play_again = input("Oops! Enter 'y' or 'n': ")

				if play_again.lower() == 'n':
					game_over = True
				elif play_again.lower() == 'y':
					pass



if __name__ == '__main__':
	main()
