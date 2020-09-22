#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
       A
    /  | \
起点   |  终点    如作图显示，起点到A的权重为6 起点到B的权重为2 B到A的权重为3 A到终点的权重为1 B到终点的权重为5
   \  | /        求起点到终点权重总和最低的路径
     B
"""


# 寻找权重最低且未处理过的节点
def find_lowest_cost_node(costs):
    lowest_cost_node = None
    lowest_cost = float('inf')
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost_node = node
            lowest_cost = cost
    return lowest_cost_node


# 起点终点有向加权图
graph = dict()
graph['start'] = dict()
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['b'] = dict()
graph['a'] = dict()
graph['b']['a'] = 3
graph['a']['end'] = 1
graph['b']['end'] = 5
graph['end'] = dict()

# 开销表
infinity = float('inf')
costs = dict()
costs['a'] = 6
costs['b'] = 2
costs['end'] = infinity

# 路径表
parents = dict()
parents['a'] = 'start'
parents['b'] = 'start'
parents['end'] = None

processed = []  # 存储处理过的节点

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if new_cost < costs[n]:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

print(costs)
print(parents)
