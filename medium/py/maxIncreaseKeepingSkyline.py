"""
In a 2 dimensional array grid, each value grid[i][j] represents the height of a
building located there. We are allowed to increase the height of any number of
buildings, by any amount (the amounts can be different for different buildings).
 Height 0 is considered to be a building as well.

At the end, the "skyline" when viewed from all four directions of the grid, i.e.
 top, bottom, left, and right, must be the same as the skyline of the original
 grid. A city's skyline is the outer contour of the rectangles formed by all
 the buildings when viewed from a distance. See the following example.

What is the maximum total sum that the height of the buildings can be increased?
"""


def maxIncreaseKeepingSkyline(grid):
    """
    violent solution
    :param grid:
    :return:
    """
    m = len(grid)  # 记录多少行
    n = len(grid[1])  # 记录多少列
    m_list = []  # 记录每行最高值
    n_list = []  # 记录每列最高值
    for i in range(m):
        m_list.append(max(grid[i]))
    for i in range(n):
        max_ = 0
        for k in range(m):
            if grid[k][i] > max_:
                max_ = grid[k][i]
        n_list.append(max_)
    nums = 0
    for m_index, list_ in enumerate(grid):
        for n_index, num in enumerate(list_):
            if num < min(m_list[m_index], n_list[n_index]):
                nums += (min(m_list[m_index], n_list[n_index]) - num)

    print(m_list, n_list, nums)
    return nums


def maxIncreaseKeepingSkyline_(grid):
    top_max = []
    left_max = []
    for i in range(len(grid)):
        left_max.append(max(grid[i]))
    for i in range(len(grid[0])):
        top_max.append(max(item[i] for item in grid))
    result = 0
    for i in range(len(top_max)):
        for j in range(len(left_max)):
            if top_max[i] < left_max[j]:
                result += top_max[i] - grid[i][j]
            else:
                result += left_max[j] - grid[i][j]
    return result


if __name__ == '__main__':
    a = maxIncreaseKeepingSkyline(
        [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]])
