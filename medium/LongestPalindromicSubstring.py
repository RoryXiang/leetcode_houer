"""[summary]
求最长回文字符串
"""


def manacher(s):
    s = '#' + '#'.join(s) + '#'  # 字符串处理，用特殊字符隔离字符串，方便处理偶数子串
    lens = len(s)
    f = []  # 辅助列表：f[i]表示i作中心的最长回文子串的长度
    maxj = 0  # 记录对i右边影响最大的字符位置j
    maxl = 0  # 记录j影响范围的右边界
    maxd = 0  # 记录最长的回文子串长度
    maxi = 0
    currentd = 0
    for i in range(lens):  # 遍历字符串
        if maxl > i:
            # 这里为了方便后续计算使用count，其表示当前字符到其影响范围的右边界的距离
            count = min(maxl - i, int(f[2 * maxj - i] / 2) + 1)
        else:
            count = 1
        # 两边扩展
        while i - count >= 0 and i + count < lens and s[i - count] == s[i + count]:
            count += 1
        if (i - 1 + count) > maxl:  # 更新影响范围最大的字符j及其右边界
            maxl, maxj = i - 1 + count, i
        f.append(count * 2 - 1)
        maxd = max(maxd, f[i])  # 更新回文子串最长长度
        if maxd > currentd:
            currentd = maxd
            maxi = i
    max_len = int((maxd - 1) / 2)
    return max_len, s[maxi - maxd // 2:maxi + maxd // 2]


if __name__ == '__main__':
    s = "abcba"
    # s = "bb"
    num, str_ = manacher(s)
    print(num, str_.replace("#", "")),
