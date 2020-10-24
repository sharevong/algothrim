#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
问题描述：接雨水
https://leetcode-cn.com/problems/trapping-rain-water/
给定n个非负整数表示每个宽度为1的柱子的高度图，计算此排列的柱子，下雨后能接多少雨水
输入：[0,1,0,2,1,0,1,3,2,1,2,1] 输出：6
"""


def trap(height):
    """
    算法思路：每根柱子能接的雨水量为它左右两边两个最高的柱子中间较低的一个柱子的高度，与它本身柱子的高度之差
    """
    if len(height) == 0:
        return 0
    left = 0
    right = len(height) - 1
    l_max = height[left]
    r_max = height[right]
    res = 0
    while left <= right:
        l_max = max(l_max, height[left])
        r_max = max(r_max, height[right])
        if l_max < r_max:
            res += l_max - height[left]
            left += 1
        else:
            res += r_max - height[right]
            right -= 1
    return res


if __name__ == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(trap(height))
