## Problem2
#Word Search(https://leetcode.com/problems/word-search/)

class Solution:
    def exist(self, board, word):
        row = len(board)
        col = len(board[0])
        directions = ((1,0),(0,1),(-1,0), (0,-1))
        
        def backtrack(board, r, c, word, idx):
            if idx == len(word):
                return True

            if r < 0 or c < 0 or r >= row or c >= col or board[r][c] != word[idx]:
                return False

            temp = board[r][c]
            board[r][c] = "#"
            
            for dr,dc in directions:
                nr = r + dr
                nc = c + dc

                if backtrack(board, nr, nc, word, idx+1):
                    return True
            #backtrack
            board[r][c] = temp
            return False

        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0]:
                    if backtrack(board, r, c, word, 0):
                        return True

        return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
sol = Solution()
print(sol.exist(board,word))
