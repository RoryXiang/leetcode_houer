# -*- coding:UTF-8 -*-

# 求岛屿面积 ===============================================
"""[summary]
Given a 2D array A, each cell is 0 (representing sea) or 1 (representing land)

A move consists of walking from one land square 4-directionally to another land square, or off the boundary of the grid.

Return the number of land squares in the grid for which we cannot walk off the boundary of the grid in any number of moves.
"""


class Solution:
    def numEnclaves(self, A):
        self.res = 0
        self.solve(A)
        return self.res

    def solve(self, board):
        if not board:
            return None

        m, n = len(board), len(board[0])

        def _solve(i, j):
            if 0 <= i < m and 0 <= j < n and board[i][j] == 1:
                board[i][j] = 2
                list(map(_solve, (i + 1, i - 1, i, i), (j, j, j + 1, j - 1)))
        print(board)
        for i in range(m):
            list(map(_solve, (i, i), (0, n - 1)))

        for i in range(n):
            list(map(_solve, (0, m - 1), (i, i)))

        for i in range(m):
            for j in range(n):
                if board[i][j] == 1:
                    board[i][j] = 0
                    self.res += 1
                elif board[i][j] == 2:
                    board[i][j] = 1


if __name__ == '__main__':
    a = Solution()
    b = a.numEnclaves([[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]])
    print(b)
