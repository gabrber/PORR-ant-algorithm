import numpy as np
import time
from aco_algorithm import AntColony

distances = np.array([[np.inf, 1, 1.5, 1, 3],
                      [1, np.inf, 1, 1.5, 2],
                      [1.5, 1, np.inf, 1, 1],
                      [1, 1.5, 1, np.inf, 2],
                      [ 3, 2, 1, 2, np.inf]])

N = 10
rand_matrix = np.random.random_integers(1,10,size=(N,N))
rand_dist = (rand_matrix + rand_matrix.T)/2
for i in range(N):
    rand_dist[i][i] = np.inf
print(rand_dist)

start_time = time.time()
ant_colony = AntColony(rand_dist, 500, 1, 4, 0.95, alpha=1, beta=1)
#ant_colony = AntColony(distances, 1, 1, 5, 0.95, alpha=1, beta=1)
shortest_path = ant_colony.run()
#shortest_path = ant_colony.run_multiprocessing()
#shortest_path = ant_colony.run_threading()
#shortest_path = ant_colony.run_threading2()

print(shortest_path)

print("--- %s seconds ---" % (time.time() - start_time))

