#!/usr/bin/env python
from aco import AntColony
import numpy as np
import json
import sys

start_num = 1
end_num = 90

#pheromone_filename = sys.argv[1]
#input_copy_filename = sys.argv[2]
pheromone_filename = "part-00000"
input_copy_filename = "input3.txt"

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
#print(type(ant_colony.pheromone))
optimal_path = ant_colony.run(start_num, end_num)
print(optimal_path)
