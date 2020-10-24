#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
问题描述：原位删除数组中的指定数值，返回移除数值后的数组长度
eg：
输入 nums=[3,2,2,3] elem=3 输出nums=[2,2,2,3] len=2
输入 nums=[0,1,2,2,3,0,4,2] elem=2 输入nums=[0,1,3,0,4,0,4,2] len=5
"""


def remove_elem(nums, elem):
    """
    算法思路：使用快慢双指针，快指针找到非移除元素时，赋值给慢指针，并移动慢指针
    """
    if len(nums) == 0:
        return 0
    slow = 0
    fast = 0
    while fast < len(nums):
        if nums[fast] != elem:
            nums[slow] = nums[fast]
            slow = slow + 1
        fast = fast + 1
    # print(nums)
    return slow


if __name__ == '__main__':
    print(remove_elem([3,2,2,3], 3))
    print(remove_elem([0,1,2,2,3,0,4,2], 2))
