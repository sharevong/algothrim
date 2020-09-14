#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
贪婪算法：解决广播台覆盖问题
"""

# 需要覆盖的美国州
states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])

# 可选的广播台及它们可覆盖的州
stations = dict()
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])

# 最后选出的广播台，数量最少且覆盖全部需要覆盖的州
final_stations = set()
while states_needed:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best_station)
print final_stations
