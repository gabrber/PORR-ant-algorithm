#!/usr/bin/env python
import sys
from aco import AntColony
import numpy as np
import json
import numpy as np
import time

start_num = 1
end_num = 90
all_time_pheromones = []
all_time_shortest_path = [None, np.inf]

for line in sys.stdin:
    line = line.strip()
    shortest_path, dic = line.split('\t', 1)
    dic = json.loads(dic)
    new_pheromone = np.asarray(dic['pheromones'])
    shortest_path = eval(shortest_path)

    if all_time_shortest_path[1] > shortest_path[1]:
        all_time_shortest_path = shortest_path

    if all_time_pheromones == []:
        all_time_pheromones = new_pheromone
    else:
        all_time_pheromones = np.add(all_time_pheromones, new_pheromone)

dic['distances'] = np.asarray(dic['distances'])
ant_colony = AntColony(dic['distances'], dic['n_ants'], 1, dic['decay'], dic['alpha'], dic['beta'], all_time_pheromones)
shortest_path, new_pheromone = ant_colony.run(start_num, end_num)

if all_time_shortest_path[1] > shortest_path[1]:
    all_time_shortest_path = shortest_path
print(all_time_shortest_path)