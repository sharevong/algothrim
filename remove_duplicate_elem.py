#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
问题描述：原位删除有序数组中存在的重复元素，返回数组中不重复元素的个数
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/
eg：输入数组[0,1,1,2,2,3,3,3]，输出4，数组变成[0,1,2,3,2,3,3,3]
"""


def remove_duplicate_elem(nums):
    """
    算法思路：使用快慢双指针，当快指针找到一个新的值时，赋值给慢指针，并移动慢指针
    """
    if len(nums) == 0:
        return 0
    slow = 0
    fast = 0
    while fast < len(nums):
        if nums[fast] != nums[slow]:
            slow = slow + 1
            nums[slow] = nums[fast]
        fast = fast + 1
    return slow + 1


if __name__ == '__main__':
    print(remove_duplicate_elem([0,1,1,2,2,3,3,3]))
