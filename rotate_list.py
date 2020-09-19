#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
问题：旋转单链表
如链表1->2->3->4->5 旋转2步变成 4->5->1->2->3
链表0->1->2 旋转4步变成 2->0->1
"""

from single_linked_list import array_to_single_linked_list


def rotate_list(linked_list, k):
    """
    算法思路：先把单链表成环，然后走len-k%len步，得到新的头节点，再断开环即可
    断开环的位置在len-k%len-1的节点处（即新的头节点在环状链表中的前一个节点）
    """
    node = linked_list.head
    l = len(linked_list)  # 计算单链表长度需要在成环之前
    while node.next:
        node = node.next
    node.next = linked_list.head  # 单链表成环

    node = linked_list.head
    i = l - k % l - 1
    while i > 0:
        node = node.next
        i -= 1
    linked_list.head = node.next
    node.next = None


if __name__ == '__main__':
    array = [1,2,3,4,5]
    linked_list = array_to_single_linked_list(array)
    rotate_list(linked_list, 2)
    print(linked_list)

    array = [0,1,2]
    linked_list = array_to_single_linked_list(array)
    rotate_list(linked_list, 4)
    print(linked_list)
