#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-26 15:29:06
# @Author  : RoryXiang (pingping19901121@gmail.com)
# @Link    : ${link}
# @Version : $Id$


def spiral_matrix(matrix):
    result = []
    m = len(matrix) - 1
    n = len(matrix[0]) - 1
    max_m = m
    min_m = 0
    max_n = n
    min_n = 0
    flag = 3
    while max_m >= min_m and max_n >= min_n:
        if flag == 3:
            add = False
            result.extend(matrix[min_m][min_n:max_n + 1])
            flag += 2 if add else -2
            min_m += 1
            continue
        if flag == 1:
            for index in range(min_m, max_m + 1):
                result.append(matrix[index][max_n])
            max_n -= 1
            flag += 2 if add else -2
            continue
        if flag == -1:
            result.extend(matrix[max_m][min_n:max_n + 1][::-1])
            flag += 2 if add else -2
            max_m -= 1
            continue
        if flag == -3:
            for index in list(range(min_m, max_m + 1))[::-1]:
                result.append(matrix[index][min_n])
            flag = 3
            min_n += 1
            continue
    if min_m == max_m and min_n == max_n:
        result.append(matrix[min_m][min_n])
    return result


if __name__ == '__main__':
    a = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    a1 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    a2 = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    b = spiral_matrix(a1)
    print(b)
