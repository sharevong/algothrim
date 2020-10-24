#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
问题描述：原位修改数组，将数组中的0移动到数组尾部
https://leetcode-cn.com/problems/move-zeroes/
eg:
输入nums=[0,1,4,0,2] 输出nums=[1,4,2,0,0]
"""


def move_zeros(nums):
    """
    算法思路：使用快慢双指针，快指针找到非0元素时，赋值给慢指针，快指针遍历完数组后，将慢指针之后的所有元素赋值为0
    """
    if len(nums) == 0:
        return nums
    slow = 0
    fast = 0
    while fast < len(nums):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow = slow + 1
        fast = fast + 1
    for i in range(slow, len(nums)):
        nums[i] = 0
    return nums


if __name__ == '__main__':
    print(move_zeros([0,1,4,0,2]))