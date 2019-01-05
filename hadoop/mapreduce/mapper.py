#!/usr/bin/env python
"""mapper.py"""
import sys
import math
import json
from aco import AntColony
import numpy as np

batch_size = 100 #this is the size of every iteration
start_num = 1
end_num = 90

for line in sys.stdin:
    line = line.strip()
    dic = line
    dic = json.loads(dic) #we make dictionary from string

    all_ants = float(dic['n_ants'])
    distances = np.asarray(dic['distances'])
    pheromones = np.asarray(dic['pheromones'])

    upper_bond = int(math.ceil(all_ants/batch_size))

    for splits_number in range(upper_bond):
        dic2 = dic.copy()
        if batch_size*(1+splits_number) < all_ants:
            dic2['n_ants'] = batch_size
            dic2['n_best'] = dic2['n_ants']
        else:
            dic2['n_ants'] = int(all_ants - splits_number*batch_size)
            dic2['n_best'] = dic2['n_ants']

        ant_colony = AntColony(distances, dic2['n_ants'], dic2['n_iterations']-1, dic2['decay'], dic2['alpha'],
                               dic2['beta'], pheromones)
        shortest_path, new_pheromone = ant_colony.run(start_num, end_num)

        dic2['distances'] = dic['distances']
        dic2['pheromones'] = dic['pheromones']

        print('%s\t%s' % (shortest_path, json.dumps(dic2)))
