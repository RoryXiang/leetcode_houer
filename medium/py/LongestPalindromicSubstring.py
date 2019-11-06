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
            count = min(maxl - i, int(f[2 * maxj - i] / 2) + 1)  # ?????
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
    return max_len, s[maxi - maxd // 2:maxi + maxd // 2].replace("#", "")


def longestPalindrome3(s):
    # https://blog.csdn.net/github_39261590/article/details/73729364
    mx = 0  # mx即为当前计算回文串最右边字符的最大值
    ans = 0
    po = 0
    Len = [0] * 10000

    # 转换字符串
    def INIT(s):
        init_s = '@#'
        for x in s:
            init_s = init_s + x + '#'

        return init_s + '$', 2 * len(s) + 1     # 字符串结尾加一个字符，防止越界

    init_s, len_s = INIT(s)  # 转换字符串
    print(init_s)
    # init_s, len_s = "#".join(s), len(s)
    get_po = 0
    for i in range(1, len_s):
        if mx > i:
            # i,j 关于po对称，所以 2po=i+j
            Len[i] = min(mx - i, Len[2 * po - i])  # 在Len[j]和mx-i 中取小,
        else:
            Len[i] = 1  # 如果i>mx，要从头开始匹配

        while init_s[i - Len[i]] == init_s[i + Len[i]]:
            Len[i] = Len[i] + 1

        if Len[i] + i > mx:  # 若新计算的回文串右端点位置大于mx，要更新po和mx的值
            mx = Len[i] + i
            po = i

        if ans < Len[i]:
            ans = Len[i]
            get_po = i

    # 返回Len[i]中的最大值-1即为原串的最长回文子串额长度
    return 'ans=  ' + str(ans - 1) + '  get_po= ' + init_s[get_po - ans + 2:get_po + ans:2]


if __name__ == '__main__':
    s = "cbabcd"
    # s = "bb"
    num, str_ = manacher(s)
    print(num, str_)

    num = longestPalindrome3(s)
    print(num)
