#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict

"""
问题描述：
给定一个数组和一个目标值，在数组中找到两个值，两个值的和为目标值，输出两个值在数组中的下标
https://leetcode-cn.com/problems/two-sum/
示例：
输入 [2,7,11,15] 9 输出 [0, 1]
时间复杂度：n
"""


def get_two_sum(arr, target):
    number_index_map = defaultdict(list)
    for i in range(len(arr)):
        x = arr[i]
        y = target - arr[i]
        number_index_map[x].append(i)
        if y in number_index_map:
            if x != y:
                return [number_index_map[y][0], i]
            elif len(number_index_map[y]) > 1:
                return [number_index_map[y][0], number_index_map[y][1]]
    return None


if __name__ == '__main__':
    assert get_two_sum([3,3], 6) == [0,1]
    assert get_two_sum([2,7,11,15], 9) == [0,1]
