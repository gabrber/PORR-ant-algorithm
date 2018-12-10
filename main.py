import numpy as np
import time
from aco_algorithm import AntColony

#np.random.seed(1000)

#distances = np.array([[np.inf, 1, 1.5, 1, 3],
#                      [1, np.inf, 1, 1.5, 2],
#                      [1.5, 1, np.inf, 1, 1],
#                      [1, 1.5, 1, np.inf, 2],
#                      [ 3, 2, 1, 2, np.inf]])

#genrate matrix
N = 500
rand_matrix = np.random.random_integers(1,100,size=(N,N))
rand_dist = (rand_matrix + rand_matrix.T)/2
for i in range(N):
    rand_dist[i][i] = np.inf

start_time = time.time()

ant_colony = AntColony(rand_dist, 20, 10, 0.95, alpha=1, beta=1)
#ant_colony = AntColony(distances, 1, 1, 5, 0.95, alpha=1, beta=1)
shortest_path = ant_colony.run(0, 5)

print("--- Final result is: ---")
print(shortest_path)
print("--- Time spent: %s seconds ---" % (time.time() - start_time))
