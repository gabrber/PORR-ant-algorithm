#!/usr/bin/env python
import sys
from aco2 import AntColony
import numpy as np
import json
import numpy as np
import time

start_num = 1
end_num = 90
all_time_pheromones = []
all_time_shortest_path = [None, np.inf]

for line in sys.stdin:
    #print(time.time(), all_time_shortest_path)
    #print(all_time_pheromones)
    line = line.strip()
    splits_number, dic = line.split('\t', 1)
    dic = json.loads(dic)
    dic['distances'] = np.asarray(dic['distances'])
    dic['pheromones'] = np.asarray(dic['pheromones'])

    ant_colony = AntColony(dic['distances'], dic['n_ants'], dic['n_iterations'], dic['decay'], dic['alpha'], dic['beta'], dic['pheromones'])
    shortest_path, new_pheromone = ant_colony.run(start_num, end_num)

    if all_time_shortest_path[1] > shortest_path[1]:
        all_time_shortest_path = shortest_path

    if all_time_pheromones == []:
        all_time_pheromones = new_pheromone
    else:
        all_time_pheromones = np.add(all_time_pheromones, new_pheromone)

ant_colony = AntColony(dic['distances'], dic['n_ants'], 1, dic['decay'], dic['alpha'], dic['beta'], dic['pheromones'])
shortest_path, new_pheromone = ant_colony.run(start_num, end_num)
if all_time_shortest_path[1] > shortest_path[1]:
    all_time_shortest_path = shortest_path
print(all_time_shortest_path)