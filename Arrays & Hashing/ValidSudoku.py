#  Link: https://leetcode.com/problems/valid-sudoku/description








# 473 / 507 test cases passed. (lol it got fixed by changing 'and not "."' to 'and board[k][l] != "."')
# [[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            columns = set()
            rows = set()
            for j in range(9):
                if board[i][j] in rows and board[i][j] != ".":
                    return False
                rows.add(board[i][j])
                if board[j][i] in columns and board[j][i] != ".":
                    return False
                columns.add(board[j][i])
            
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = set()
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        if board[k][l] in box and not ".":
                            return False
                        box.add(board[k][l])
        return True