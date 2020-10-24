#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
问题描述：给定一个数组和一个数字，找到数组中的两个数，使它们相加等于给定的数字，数组是有序的，升序
https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/
输入：[2,7,11,15]  输出：[0,1]
"""


def two_sum_sorted(arr, target):
    """
    算法思路：使用双指针，一个指向数组第一个元素，一个指向数组最后一个元素
    判断两数之和与给定数字的大小关系，分别移动头尾指针
    """
    left = 0
    right = len(arr)-1
    while left < right:
        two_sum = arr[left] + arr[right]
        if two_sum > target:
            right -= 1
        elif two_sum < target:
            left += 1
        else:
            return [left, right]
    return None


if __name__ == '__main__':
    assert two_sum_sorted([2,7,11,15], 9) == [0,1]
