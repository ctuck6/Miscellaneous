#include "Sudoku.hpp"

void Sudoku::solveSudoku(Board &board) {
    solveCell(board, 0, 0);
}

/*
    Starts at row 0. Solves every column in that row.
    When we reach the last column we move to the next row.
    Once the last row finishes, we know its over and the board is solved!
*/
bool Sudoku::solveCell(Board &board, int row, int col) {
    if (col == BOARD_SIZE) { // Checks if the row is done. If so, move to the beginning of next row
        col = 0; // Start at the beginning of row
        row++; // Move to next row

        if (row == BOARD_SIZE) { // We are dome
            return true;
        }
    }

    // Dont change the filled cells. Go to next column
    if (board.getIndex(row, col) != EMPTY_ENTRY) {
        return solveCell(board, row, col + 1);
    }

    // Try all values in the cell
    for (int value = 1; value <= BOARD_SIZE; value++) {
        if (isValid(board, row, col, value)) {
            board.updateBoard(row, col, value);

            if (solveCell(board, row, col + 1)) { // If its a valid move, continue
                return true;
            }
        }

    }

    // Revert the cell because we cannot go further from this state
    board.updateBoard(row, col, EMPTY_ENTRY);

    return false; // No valid number works for this cell
}

bool Sudoku::isValid(Board board, int row, int col, int num) {
    // Check row validity
    for (int i = 0; i < BOARD_SIZE; i++) {
        if (num == board.getIndex(row, i)) {
            return false;
        }
    }

    // Check column validity
    for (int i = 0; i < BOARD_SIZE; i++) {
        if (num == board.getIndex(i, col)) {
            return false;
        }
    }

	////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

	// !IMPORTANT! Computes top left of the subGrid that (row, col) fall into
	int subGridSize = sqrt(BOARD_SIZE);
	int leftCornerY = subGridSize * (row / subGridSize);
    int leftCornerX = subGridSize * (col / subGridSize);

	////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    // Traverse sub grid
    for (int i = 0; i < subGridSize; i++) {
        for (int j = 0; j < subGridSize; j++) {
            if (num == board.getIndex(leftCornerY + i, leftCornerX + j)) {
                return false;
            }
        }
    }

    return true; // The cell is valid
}
