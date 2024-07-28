## Problem1 
#N Queens(https://leetcode.com/problems/n-queens/)
class Solution:
    def solveNQueens(self, n):
        def isSafe(board,r,c):
            for i in range(r):
                if board[i][c] == "Q":
                    return False

            i, j = r, c
            while (i >= 0 and j < n):
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1

            i, j = r, c
            while (i >= 0 and j >= 0):
                if board[i][j] == "Q":
                    return False

                i -= 1
                j -= 1

            return True


        def backtrack(board, r):
            if r == len(board):
                res.append([''.join(row) for row in board])
            
            for c in range(len(board)):
                if isSafe(board, r, c):
                    board[r][c] = "Q"
                    backtrack(board, r + 1)
                    board[r][c] = "."

        res = []
        board = [['.'] * n for _ in range(n)]
        backtrack(board, 0) 
        return res

n = 4
sol = Solution()
print(sol.solveNQueens(n))