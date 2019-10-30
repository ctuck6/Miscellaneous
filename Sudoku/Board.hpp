#ifndef Board_hpp
#define Board_hpp

#include <iostream>

using namespace std;

const int EMPTY_ENTRY = 0;
const int BOARD_SIZE = 9;

class Board {
	private:
		int board[BOARD_SIZE][BOARD_SIZE];

	public:
		Board(int [BOARD_SIZE][BOARD_SIZE]); // Initializes the Sudoku board
		void updateBoard(int, int, int); // Updates the state of the board
		int getIndex(int, int); // Gets the value at index (row, col)
		void printBoard(); // Prints the Sudoku board
};

#endif /* Board_hpp */
