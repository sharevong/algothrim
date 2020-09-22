#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
使用广度优先算法检查朋友中是否有芒果销售商
"""

from collections import deque


# 判断一个人是否是芒果销售商的方法：名字最后一个字母为m
def person_is_seller(name):
    return name[-1] == 'm'


# 广度优先搜索
def bfs(graph, start):
    search_queue = deque()
    search_queue += graph[start]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + " is a mango seller")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


# 朋友关系图
graph = dict()
graph['you'] = ['alice', 'bob', 'claire']
graph['alice'] = ['peggy']
graph['bob'] = ['anuj', 'peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = ['']
graph['peggy'] = ['']
graph['thom'] = ['']
graph['jonny'] = ['']
print(bfs(graph, 'you'))


