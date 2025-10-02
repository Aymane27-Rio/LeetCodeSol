// Link: https://leetcode.com/problems/valid-sudoku/description


// Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

// Each row must contain the digits 1-9 without repetition.
// Each column must contain the digits 1-9 without repetition.
// Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
// Note:

// A Sudoku board (partially filled) could be valid but is not necessarily solvable.
// Only the filled cells need to be validated according to the mentioned rules.




/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
    for (let i = 0; i < 9; i++) {
        const seen = new Set();
        for (let j = 0; j < 9; j++) {
            const cell = board[i][j];
            if (cell !== '.') {
                if (seen.has(cell)) {
                    return false;
                }
                seen.add(cell);
            }
        }
    }
    for (let j = 0; j < 9; j++) {
        const seen = new Set();
        for (let i = 0; i < 9; i++) {
            const cell = board[i][j];
            if (cell !== '.') {
                if (seen.has(cell)) {
                    return false;
                }
                seen.add(cell);
            }
        }
    }
    for (let row = 0; row < 9; row += 3) {
        for (let col = 0; col < 9; col += 3) {
            const seen = new Set();
            for (let i = row; i < row + 3; i++) {
                for (let j = col; j < col + 3; j++) {
                    const cell = board[i][j];
                    if (cell !== '.') {
                        if (seen.has(cell)) {
                            return false;
                        }
                        seen.add(cell);
                    }
                }
            }
        }
    }
    return true;
};