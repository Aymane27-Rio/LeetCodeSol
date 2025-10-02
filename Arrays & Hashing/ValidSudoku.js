// Link: https://leetcode.com/problems/valid-sudoku/description






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