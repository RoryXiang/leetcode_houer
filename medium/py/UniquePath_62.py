"""
leetcode 62
解题思路：每个点只能从左边和上边下来，所以到达当前点的所有路径数为，到达左边点的总路
径数+到达上边点的总路径数。另外，到达第一行、第一列的的任何一个点的路径数为1
"""


def unique_path(m, n):
    if m <= 0 or n <= 0:
        return 0
    res = [0 for _ in range(0, n)]
    res[0] = 1
    for i in range(0, m):
        for j in range(1, n):
            res[j] += res[j - 1]

        print(res)
    return res[n - 1]


if __name__ == '__main__':
    m = 7
    n = 3
    result = unique_path(m, n)
    print(result)
