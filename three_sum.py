#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
问题描述：
给定一个数组和一个目标值，在数组中找出三个数，使它们的和为目标值（two_sum的升级问题）
示例：
输入[-1,0,1,2,-1,-4] 0 输出[[-1,0,1], [-1,-1,2]]
说明：
输出为数组元素的值，而不是元素的下标，不能包含重复的三个数的组合
"""


def three_sum(arr, target):
    """
    算法思路：
    排序后从头到尾遍历数组元素，如取第一个元素，则在剩下的数组元素中取另外两个元素，使两个元素的和为目标值减去第一个元素的值
    取两个元素使用双指针的方法，一个在头，一个在尾，当头尾两个元素的和超过需要补充的值，则尾指针向前移（减少头尾指针和）
    当头尾两个元素的和小于需要补充的值，则头指针向后移（增大头尾指针和），
    当头尾两个元素的和等于需要补充的值，则和第一个元素构成一个符合要求的三元组。
    由于不能包含重复的三元组，遍历数组元素及头尾指针移动时，需跳过重复元素。
    时间复杂度：n^2
    """
    arr.sort()
    result = list()
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:  # 跳过重复出现的值
            continue
        j = i+1
        k = len(arr) - 1
        while j < k:
            if arr[j] + arr[k] > target - arr[i]:
                k = k-1
            elif arr[j] + arr[k] < target - arr[i]:
                j = j+1
            else:
                result.append([arr[i], arr[j], arr[k]])
                j = j+1
                k = k-1
                while j < k and arr[j] == arr[j-1]:  # 跳过重复出现的值
                    j = j+1
                while j < k and arr[k] == arr[k+1]:  # 跳过重复出现的值
                    k = k-1
    return result


if __name__ == '__main__':
    arr = [-1,0,1,2,-1,-4]
    target = 0
    print three_sum(arr, target)

    arr = [-4,0,1,2,2,2,2,4]
    print three_sum(arr, target)
