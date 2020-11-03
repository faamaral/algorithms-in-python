import os

from collections import defaultdict

def extract_data_r(file_name, mode):
    graph = {}

    with open(os.path.abspath(file_name), mode) as file:

        for line in file:
            city_1, city_2, dist = line.strip().split(',')
            dist = int(dist)
            if city_1 not in graph:
                graph[city_1] = {city_2: dist}
            else:
                graph[city_1, city_2] = dist

            if city_2 not in graph:
                graph[city_2] = {city_1: dist}
            else:
                graph[city_2][city_1] = dist
    return graph



def extract_data(file_name):
    graph = defaultdict(list)

    with open(os.path.abspath(file_name), 'r') as file:

        for string in file.readlines():
            line = string.strip().split(',')
            graph[line[0]].append({line[1]: line[2]})
            graph[line[1]].append({line[0]: line[2]})
    return graph

