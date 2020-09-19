#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给定一个整数数组和一个整数k，找出数组中和为k的连续子数组的个数
输入：nums=[1,1,1] k = 2,  输出2，符合要求的子数组为[1,1],[1,1]
输入：nums=[3,5,2,-2,4,1], 输出4，符合要求的子数组为[5], [5,2,-2], [2,-2,4,1], [4,1]
"""


def sub_array_sum(arr, k):
    """
    算法思路：使用数组的前缀和，计算数组前N个位置每个位置对应的从0到N的子数组的和
    在计算每个位置的子数组和sum(i)时，同时检查是否已存在和为sum(i)-k的子数组（假设为sum(j)）
    则[j+1,i]则为一个符合条件的子数组
    """
    pre_sum = dict()
    tmp = 0
    ans = 0
    pre_sum[0] = [-1]  # 基本情况，空的子数组和为0，对应下标取-1
    for i in range(len(arr)):
        tmp += arr[i]
        if pre_sum.get(tmp-k) is not None:
            ans += len(pre_sum.get(tmp-k))
        if pre_sum.get(tmp) is None:
            pre_sum[tmp] = [i]
        else:
            pre_sum[tmp].append(i)
    # print(pre_sum)
    return ans


if __name__ == '__main__':
    print(sub_array_sum([1,1,1], 2))
    print(sub_array_sum([3,5,2,-2,4,1], 5))
