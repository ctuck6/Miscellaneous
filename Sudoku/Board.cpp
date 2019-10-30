#include "Board.hpp"

Board::Board(int inputArr[BOARD_SIZE][BOARD_SIZE]) {
    for (int row = 0; row < BOARD_SIZE; row++) {
        for (int col = 0; col < BOARD_SIZE; col++) {
             board[row][col] = inputArr[row][col];
        }
    }
}

void Board::updateBoard(int row, int col, int value) {
    board[row][col] = value;
}

int Board::getIndex(int row, int col) {
    return board[row][col];
}

void Board::printBoard() {
    cout << "╔═════════╦═════════╦═════════╗" << endl;

    for (int i = 0; i < BOARD_SIZE; i++) {
        cout << "║";

        for (int j = 0; j < BOARD_SIZE; j++) {
            cout << " " << board[i][j] << " ";

            if (((j + 1) % 3) == 0) {
                cout << "║";
            }
        }

        cout << endl;

        if (((i + 1) % 3) == 0 and (i != 8 )) {
            cout << "╠═════════╬═════════╬═════════╣" << endl;
        }
    }

    cout << "╚═════════╩═════════╩═════════╝" << endl << endl;
    // Found these fancy borders on the web :)
}
