#!/usr/bin/env python
import sys
import ast
from aco import AntColony
import numpy as np
import json

start_num = 1
end_num = 90
init_pheromone = []

for line in sys.stdin:
    line = line.strip()
    splits_number, dic = line.split('\t', 1)
    dic = json.loads(dic)
    dic['distances'] = np.asarray(dic['distances'])
    dic['pheromones'] = np.asarray(dic['pheromones'])

    if init_pheromone == []:
        init_pheromone = dic['pheromones']

    #dic['distances'] = eval(dic['distances'])

    ant_colony = AntColony(dic['distances'], dic['n_ants'], dic['n_iterations'], dic['decay'], dic['alpha'], dic['beta'], dic['pheromones'])
    #ant_colony['pheromones'] = dic['pheromones']
    new_pheromone = ant_colony.run_reducer(start_num, end_num)
    init_pheromone = np.add(init_pheromone, new_pheromone)
out_pheromone = {'pheromones':init_pheromone.tolist()}
#out_pheromone = {'pheromones':init_pheromone}
print('%s' % json.dumps(out_pheromone))