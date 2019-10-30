#include "Board.cpp"
#include "Sudoku.cpp"
#include <iostream>

using namespace std;

/*
	Reads in the users input as the board.
	If the input is invalid, the function will return false and make you enter a new board
*/
bool readBoard(int [BOARD_SIZE][BOARD_SIZE]);

int main(int argc, char const *argv[]) {
	int inputArr[BOARD_SIZE][BOARD_SIZE];

	while (!readBoard(inputArr)) {
		cout << "Invalid input!" << endl;
	}

    Board board = Board(inputArr);
    Sudoku sudoku;

    cout << "The original Sudoku board is:" << endl << endl;
    board.printBoard();
    sudoku.solveSudoku(board);
    cout << "The solution Sudoku board is:" << endl << endl;
    board.printBoard();

	return 0;
}

bool readBoard(int inputArr[BOARD_SIZE][BOARD_SIZE]) {
    cout << "Enter below the solution: " << endl;

    for (int row = 0; row < BOARD_SIZE; row++) {
        for (int col = 0; col < BOARD_SIZE; col++) {
            cin >> inputArr[row][col];

            if (inputArr[row][col] < EMPTY_ENTRY or inputArr[row][col] > BOARD_SIZE) {
            	return false;
            }
        }
    }

    cout << endl;

    return true;
}
