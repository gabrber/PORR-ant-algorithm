import numpy as np

from aco_algorithm import AntColony

distances = np.array([[np.inf, 1, 1.5, 1],
                      [1, np.inf, 1, 1.5],
                      [1.5, 1, np.inf, 1],
                      [1, 1.5, 1, np.inf]])


ant_colony = AntColony(distances, 1, 1, 100, 0.95, alpha=1, beta=1)
shortest_path = ant_colony.run()
print(shortest_path)
