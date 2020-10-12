#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
问题描述：求两个字符串的最长公共子串的长度
eg: str1 abcdefgh str2 acef 的最长公共子串为 acef，长度为4
"""


def max_sub_str_len(str1, str2):
    """
    算法思路：动态规划
    dp[i][j]代表字符串str1[0...i]和字符串str2[o...j]的最长公共子串的长度
    状态转移方程为
    dp[i][j] = dp[i-1][j-1] + 1 当str1[i] = str2[j]
    dp[i][j] = max(dp[i][j-1], dp[i-1][j]) 当str1[i] != str2[j]
    base case为str1或str2为空串，此时公共子串的长度为0
    """
    str1 = ' ' + str1  # 在两个字符串前加空格作为base case
    str2 = ' ' + str2
    l1 = len(str1)
    l2 = len(str2)
    l = [[0] * l1 for i in range(l2)]
    for i in range(1, l2):
        for j in range(1, l1):
            if str2[i] == str1[j]:
                l[i][j] = l[i-1][j-1] + 1
            else:
                l[i][j] = max(l[i-1][j], l[i][j-1])
    return l[l2-1][l1-1]


if __name__ == '__main__':
    print(max_sub_str_len('abcdefgh', 'acef'))
    print(max_sub_str_len('abcdefgh', 'achg'))
