import numpy as np
import json

# Basic initial data

dic = {'n_ants': 800, 'n_best': 800, 'n_iterations': 10, 'decay': 0.95, 'alpha': 1, 'beta': 1}
N = 500

# Generate random distance matrix

rand_matrix = np.random.random_integers(1,1000,size=(N,N))
rand_dist = (rand_matrix + rand_matrix.T)/2
for i in range(N):
    rand_dist[i][i] = np.inf
print(rand_dist)

dic['distances'] = np.array(rand_dist).tolist()

# Add initial pheromone

pheromones = np.ones(rand_dist.shape) / len(rand_dist)

dic['pheromones'] = pheromones.tolist()
print(len(dic['pheromones']))
# Save to file as json
print(str(dic))
with open('./data/inp', 'w') as file:
     file.write(json.dumps(dic))

