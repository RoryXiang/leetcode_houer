# coding=utf-8
import copy
import operator
from collections import Counter


def result(secret, guess):
    """先找到位置数字都对应的，然后在比较数字和位置不对应的"""
    result = "{}A{}B"
    A = 0
    B = 0
    secret_un = []  # 存放secret中和guess没匹配上的
    secret_ = ""  # 存放secret中和guess没匹配上的
    guess_ = ""  # 存放guess中和secret没匹配上的
    for index, num in enumerate(guess):
        if num == secret[index]:
            A += 1
        else:
            secret_un.append(secret[index])
            secret_ += secret[index]
            guess_ += guess[index]
    for index, num in enumerate(guess_):
        if num in secret_un:
            B += 1
            secret_un.remove(num)

    return result.format(A, B)


def result1(secret, guess):
    # 最快
    bulls = sum(map(operator.eq, secret, guess))
    both = sum(min(secret.count(x), guess.count(x)) for x in set(guess))
    return '%dA%dB' % (bulls, both - bulls)


def result2(secret, guess):
    s, g = Counter(secret), Counter(guess)
    a = sum(i == j for i, j in zip(secret, guess))
    return '%sA%sB' % (a, sum((s & g).values()) - a)


if __name__ == '__main__':
    a = result1("1122", "1222")
    print(a)
