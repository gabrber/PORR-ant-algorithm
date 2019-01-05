#!/usr/bin/env python
from aco import AntColony
import numpy as np
import json
import sys

start_num = 1
end_num = 90

input_copy_filename = "../data/input500_10_800.txt"

file_input_copy = open(input_copy_filename, "r")

for input_copy in file_input_copy:
    dic = input_copy.strip()

dic = json.loads(dic)

dic['distances'] = np.asarray(dic['distances'])

ant_colony = AntColony(dic['distances'], dic['n_ants'], dic['n_iterations'], dic['decay'], dic['alpha'], dic['beta'])

optimal_path = ant_colony.run(start_num, end_num)

print(optimal_path[1])