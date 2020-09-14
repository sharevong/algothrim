#!/usr/bin/env python
# -*- coding: utf-8 -*

"""
换酒问题：
小区便利店正在促销，用numExchange个空酒瓶可以兑换一瓶酒，购入numBottles瓶酒后最多可以喝到多少瓶酒
示例：
numExchange=3,numBottles=9, 最多喝到9+3+1=13瓶酒
numExchange=4,numBottles=15, 最多能喝到15+3+1=19瓶酒
numExchange=5,numBottles=5, 最多能喝到5+1=6瓶酒
numExchange=3,numBottles=2, 最多能喝到2瓶酒
"""


def max_drink(num_exchange, num_bottles):
    total = num_bottles
    while num_bottles >= num_exchange:
        change = num_bottles / num_exchange
        total += change
        num_bottles = change + num_bottles % num_exchange
    return total


print max_drink(3, 9)
print max_drink(4, 15)
print max_drink(5, 5)
print max_drink(3, 2)
