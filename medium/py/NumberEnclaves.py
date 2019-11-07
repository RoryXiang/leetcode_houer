# -*- coding:UTF-8 -*-

# 求岛屿面积 ======================================================
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
            if i == 2 and j == 2:
                print(board[i][j], 0 <= i < m and 0 <=
                      j < n and board[i][j] == 1, "???????????")
            if 0 <= i < m and 0 <= j < n and board[i][j] == 1:
                # print("????", i, j)
                board[i][j] = 2
                # print(board)
                list(map(_solve, (i + 1, i - 1, i, i), (j, j, j + 1, j - 1)))

        # 从所有行的开始和结尾往里，如果边缘是1则换成2，往里走
        for i in range(m):
            list(map(_solve, (i, i), (0, n - 1)))
        # 从所有列的开始和结尾往里，如果边缘是1则换成2，往里走
        for i in range(n):
            list(map(_solve, (0, m - 1), (i, i)))
        # print(board)
        # 最后统计所有的1，就是岛屿面积
        for i in range(m):
            for j in range(n):
                if board[i][j] == 1:
                    self.res += 1
                elif board[i][j] == 2:
                    board[i][j] = 1


if __name__ == '__main__':
    a = Solution()
    b = a.numEnclaves([[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]])
    print(b)
