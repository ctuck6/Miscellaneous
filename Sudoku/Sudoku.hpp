#ifndef Sudoku_hpp
#define Sudoku_hpp

#include "Board.hpp"
#include <math.h>
#include <iostream>

using namespace std;

class Sudoku {
	public:
		void solveSudoku(Board &); // Calls solveCell which recursively solves the board with backtracking
		bool solveCell(Board &, int, int); // Main recursive backtracking function to solve the board
		bool isValid(Board, int, int, int); // Returns true if the cell is valid, else false

};

#endif /* Sudoku_hpp */
