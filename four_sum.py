#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict

"""
问题描述：
给定一个数组和一个目标值，在数组中找出四个元素，使它们的和为目标值
https://leetcode-cn.com/problems/4sum/
示例：
输入[1,0,-1,0,-2,2] 0 输出[[-1,0,0,1], [-2,-1,1,2], [-2,0,0,2]]
说明：
输出的是元素值，而不是元素下标，不包含重复，从输出结果可以看出，数组做了排序
"""


def four_sum(arr, target):
    """
    算法思路：
    首先把数组中所有二元组的two_sum记录下来存在dict中，然后再在这个dict中找到能满足和为目标值的两个二元组
    为了避免出现重复数据，限制第一个二元组的第二个元素的下标小于第二个二元组的第一个元素的下标
    即a < b < i < j,假设a b i j为四个元素分别对应的下标
    时间复杂度：n^2
    """
    result = list()
    arr.sort()
    two_sum_dict = defaultdict(list)

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            two_sum = arr[i] + arr[j]
            two_sum_dict[two_sum].append([i, j])

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if j > i+1 and arr[j] == arr[j-1]:
                continue
            two_sum = arr[i] + arr[j]
            another_two_sum = two_sum_dict.get(target - two_sum)
            if another_two_sum is None:
                continue
            for pair in another_two_sum:
                if pair[0] > j:
                    a = pair[0]
                    b = pair[1]
                    result.append([arr[i], arr[j], arr[a], arr[b]])

    tmp = []
    for i in result:
        if i not in tmp:
            tmp.append(i)
    return tmp


if __name__ == '__main__':
    assert four_sum([-2,-1,-1,1,1,1,2,2], 0) == [[-2,-1,1,2], [-1,-1,1,1]]
    assert four_sum([1,0,-1,0,-2,2], 0) == [[-2,-1,1,2], [-2,0,0,2], [-1,0,0,1]]
