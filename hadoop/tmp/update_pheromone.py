#!/usr/bin/env python
import sys
import ast
from aco import AntColony
import numpy as np
import json

pheromone_filename = sys.argv[1]
input_copy_filename = sys.argv[2]

file_pheromone = open(pheromone_filename, "r")
file_input_copy = open(input_copy_filename, "r")

for pheromone in file_pheromone:
    new_pheromone = pheromone

for input_copy in file_input_copy:
    dic = input_copy.strip()

dic = json.loads(dic)
new_pheromone = json.loads(new_pheromone)

dic['distances'] = np.asarray(dic['distances'])
dic['pheromones'] = np.asarray(new_pheromone['pheromones'])

ant_colony = AntColony(dic['distances'], dic['n_ants'], dic['n_iterations'], dic['decay'], dic['alpha'], dic['beta'], dic['pheromones'])
ant_colony.update_pheromone()

dic['distances'] = np.array(dic['distances']).tolist()
dic['pheromones'] = dic['pheromones'].tolist()

#print(dic['pheromones'])

with open('./'+sys.argv[2], 'w') as file:
    file.write(json.dumps(dic))


