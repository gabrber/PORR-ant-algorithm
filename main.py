import numpy as np
import time
import json
from random import randrange
from aco_algorithm import AntColony

#np.random.seed(1000)

# MANUAL
#
#distances = np.array([[np.inf, 1, 1.5, 1, 3],
#                      [1, np.inf, 1, 1.5, 2],
#                      [1.5, 1, np.inf, 1, 1],
#                      [1, 1.5, 1, np.inf, 2],
#                      [ 3, 2, 1, 2, np.inf]])

# GENERATE
#
#N = 10
#rand_matrix = np.random.random_integers(1,100,size=(N,N))
#rand_dist = (rand_matrix + rand_matrix.T)/2
#for i in range(N):
#    rand_dist[i][i] = np.inf
#for i in range((int) (N/10)):
#    j = randrange(0,N-1)
#    k = randrange(0,N-1)
#    rand_dist[j][k] = np.inf
#    rand_dist[k][j] = np.inf
#
#pheromone = np.ones(rand_dist.shape) / len(rand_dist)
#
#ant_colony = AntColony(rand_dist, 20, 100, 0.95, pheromone, alpha=1, beta=1)
#
#start_time = time.time()
#shortest_path = ant_colony.run(0, 5)

# FROM JSON

json_file = open('spark/files/input.txt')
json_str = json_file.read()
json_data = json.loads(json_str)

distances = np.asarray(json_data['distances'])
pheromones = np.asarray(json_data['pheromones'])
ant_colony = AntColony(distances, json_data['n_ants'], json_data['n_iterations'], json_data['decay'], pheromones, json_data['alpha'], json_data['beta'])

start_time = time.time()
shortest_path = ant_colony.run(json_data['start_point'], json_data['end_point'])

print("--- Final result is: ---")
print(shortest_path)
print("--- Time spent: %s seconds ---" % (time.time() - start_time))
