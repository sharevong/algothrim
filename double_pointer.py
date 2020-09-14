#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
问题描述：
给定n个非负整数a1, a2, ... an,每个数代表坐标系中的一个点（i, ai）。
在坐标系内画n条垂直线，垂直线i的两个端点分别为（i, ai）(i, 0)。
找出其中的两条线，使得它们与x轴共同构成的容器可以容纳最多的水。
说明：不能倾斜容器，n的值最少为2
示例：
输入[1,8,6,2,5,4,8,3,7] 输出49
"""


def get_max_volumn(numbers):
    """
    算法思路：
    使用双指针分别指向数组的头尾，此时为头尾两个元素的较小值能构成的最大面积（此时距离最大宽度最长）
    然后把较小值对应的指针向中间靠拢，继续找新的头尾元素对应的较小值能构成的最大面积
    重复上述步骤，直到头尾两个指针相遇
    """
    i = 0
    j = len(numbers)-1
    result = 0
    while i < j:
        tmp = min(numbers[i], numbers[j]) * (j-i)
        result = max(tmp, result)
        if numbers[i] < numbers[j]:
            i = i+1
        else:
            j = j-1
    return result


if __name__ == '__main__':
    numbers = [1,8,6,2,5,4,8,3,7]
    print get_max_volumn(numbers)
