#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
问题：有N个航班，编号从1到，已知存在一个航班预定表，表中的第i条记录bookings[i]=[i,j,k]
表示航班i到j预定了k个座位，已知航班预定表，求各个航班的总预定数
输入：bookings=[[1,2,10], [2,3,20], [2,5,25]] N=5
输出：[10,55,45,25,25]
"""


class DifferenceArray(object):
    """
    算法思路：使用差分数组，实现简单的对数组部分区间进行加减的操作
    示例数组：8,2,6,3,1
    对应差分数组:8,-6,4,-3,-2

    假如想要对原始数组的第2到4个元素进行加3操作，则将差分数组的第2个元素加3，第5个元素减3即可
    变化差分数组:8,-3,4,-3,-5
    对应变化数组:8,5,9,6,1
    """
    def __init__(self, array):
        self.array = array
        self.diff_arr = list()
        for i in range(len(array)):
            if i == 0:
                self.diff_arr.append(self.array[i])
            else:
                self.diff_arr.append(self.array[i] - self.array[i-1])

    def increment(self, i, j, k):
        self.diff_arr[i] += k
        if j+1 < len(self.array):
            self.diff_arr[j+1] -= k
        for i in range(len(self.diff_arr)):
            if i == 0:
                self.array[i] = self.diff_arr[i]
            else:
                self.array[i] = self.array[i-1] + self.diff_arr[i]


if __name__ == '__main__':
    bookings = [[1,2,10], [2,3,20], [2,5,25]]
    array = [0 for i in range(5)]
    difference_array = DifferenceArray(array)
    for idx in range(len(bookings)):
        i = bookings[idx][0]-1  # 数组下标从0开始，所以需要减1
        j = bookings[idx][1]-1
        k = bookings[idx][2]
        difference_array.increment(i, j, k)
    print(difference_array.array)
