#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
单链表的python实现
"""


class Node(object):
    def __init__(self, n):
        self.elem = n
        self.next = None


class SingleLinkedList(object):
    def __init__(self, node=None):
        self.head = node

    def append(self, n):
        """
        在链表尾部增加元素
        """
        node = Node(n)
        if self.head is None:
            self.head = node
        else:
            tmp = self.head
            while tmp.next is not None:
                tmp = tmp.next
            tmp.next = node

    def remove(self, elem):
        """
        删除元素elem,删除第一个出现的元素
        """
        tmp = self.head
        prev = None
        while tmp:
            if tmp.elem == elem:
                if tmp == self.head:
                    self.head = tmp.next
                else:
                    prev.next = tmp.next
                break
            else:
                prev = tmp
                tmp = tmp.next

    def __len__(self):
        l = 0
        tmp = self.head
        while tmp:
            l += 1
            tmp = tmp.next
        return l

    def __str__(self):
        arr = list()
        tmp = self.head
        while tmp is not None:
            arr.append(tmp.elem)
            tmp = tmp.next
        return str(arr)

    __repr__ = __str__


def array_to_single_linked_list(arr):
    single_linked_list = SingleLinkedList()
    for i in range(len(arr)):
        single_linked_list.append(arr[i])
    return single_linked_list


if __name__ == '__main__':
    array = [1,2,3,4,5]
    single_linked_list = array_to_single_linked_list(array)
    print(single_linked_list)
    single_linked_list.remove(4)
    print(single_linked_list)
    print(len(single_linked_list))
