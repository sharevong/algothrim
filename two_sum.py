#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
问题描述：
给定一个数组和一个目标值，在数组中找到两个值，两个值的和为目标值，输出两个值在数组中的下标
示例：
输入 [2,7,11,15] 9 输出 [0, 1]
时间复杂度：n
"""


def get_two_sum(arr, target):
    number_index_map = dict()
    for i in range(len(arr)):
        number_index_map[arr[i]] = i
        j = number_index_map.get(target - arr[i])
        if j is not None:
            return [j, i]
    return None


if __name__ == '__main__':
    arr = [2,7,11,15]
    target = 9
    print get_two_sum(arr, target)
