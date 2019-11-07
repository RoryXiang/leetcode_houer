"""
leetcode 64
"""


def minPathSum(grid):
    if grid is None:
        return 0
    if len(grid) <= 1:
        return sum(grid[0])
    if len(grid[0]) <= 1:
        sum_result = 0
        for loc in grid:
            sum_result += sum(loc)
        return sum_result

    row = len(grid)
    loc = len(grid[0])
    dp = grid
    for i in range(1, row):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    for i in range(1, loc):
        dp[0][i] = dp[0][i - 1] + grid[0][i]
    for i in range(1, row):
        for j in range(1, loc):
            dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
    return dp[i][j]


if __name__ == '__main__':
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    # grid = [[0], [1]]
    min_sum = minPathSum(grid)
    print(min_sum)
