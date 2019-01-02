import numpy as np
import time
from random import randrange
from aco_algorithm import AntColony

#np.random.seed(1000)

#distances = np.array([[np.inf, 1, 1.5, 1, 3],
#                      [1, np.inf, 1, 1.5, 2],
#                      [1.5, 1, np.inf, 1, 1],
#                      [1, 1.5, 1, np.inf, 2],
#                      [ 3, 2, 1, 2, np.inf]])

#genrate matrix
N = 10
rand_matrix = np.random.random_integers(1,100,size=(N,N))
rand_dist = (rand_matrix + rand_matrix.T)/2
for i in range(N):
    rand_dist[i][i] = np.inf
for i in range((int) (N/10)):
    j = randrange(0,N-1)
    k = randrange(0,N-1)
    rand_dist[j][k] = np.inf
    rand_dist[k][j] = np.inf

start_time = time.time()

pheromone = np.ones(self.distances.shape) / len(rand_dist)
ant_colony = AntColony(rand_dist, 20, 100, 0.95, pheromone, alpha=1, beta=1)
#ant_colony = AntColony(distances, 1, 1, 5, 0.95, alpha=1, beta=1)
shortest_path = ant_colony.run(0, 5)

print("--- Final result is: ---")
print(shortest_path)
print("--- Time spent: %s seconds ---" % (time.time() - start_time))
