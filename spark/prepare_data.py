import numpy as np
import json

# Basic initial data

dic = {'n_ants': 1, 'n_iterations': 1, 'decay': 0.95, 'alpha': 1, 'beta': 1}
N = 10

# Generate random distance matrix

rand_matrix = np.random.random_integers(1,10,size=(N,N))
rand_dist = (rand_matrix + rand_matrix.T)/2
for i in range(N):
    rand_dist[i][i] = np.inf
print(rand_dist)

dic['distances'] = rand_dist.tolist()

# Add initial pheromone

pheromones = np.ones(rand_dist.shape) / len(rand_dist)
dic['pheromones'] = pheromones.tolist()

# Save to file as json

with open('files/input.txt', 'w') as file:
    file.write(json.dumps(dic))