"""
leetcode 63
思路： 将原始转移矩阵能通过改为1，路障改为0（可以认为是当前点的通行系数），没经过一个位置，用通过这个位置之前的路径数总和乘以当前点的系数
"""


def unique_path_2(obstacleGrid):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    obstacleGrid[0][0] = 0 if obstacleGrid[0][0] else 1
    for i in range(1, m):
        obstacleGrid[i][0] = \
            0 if obstacleGrid[i][0] or not obstacleGrid[i - 1][0] else 1
    for i in range(1, n):
        obstacleGrid[0][i] = \
            0 if obstacleGrid[0][i] or not obstacleGrid[0][i - 1] else 1
    for i in range(1, m):
        for j in range(1, n):
            obstacleGrid[i][j] = 0 if obstacleGrid[i][j] else 1
            obstacleGrid[i][j] = \
                (obstacleGrid[i][j - 1] + obstacleGrid[i - 1][j]) * \
                obstacleGrid[i][j]
    return obstacleGrid[-1][-1]
