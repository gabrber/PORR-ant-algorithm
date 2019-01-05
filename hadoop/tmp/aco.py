#!/usr/bin/env python
import numpy as np
from numpy.random import choice as np_choice

class AntColony():

    def __init__(self, distances, n_ants, n_iterations, decay, alpha=1, beta=1, pheromone=[]):
        """
        Args:
            distances (2D numpy.array): Square matrix of distances. Diagonal is assumed to be np.inf.
            n_ants (int): Number of ants running per iteration
            n_iteration (int): Number of iterations
            decay (float): Rate it which pheromone decays. The pheromone value is multiplied by decay, so 0.95 will lead to decay, 0.5 to much faster decay.
            alpha (int or float): exponenet on pheromone, higher alpha gives pheromone more weight. Default=1
            beta (int or float): exponent on distance, higher beta give distance more weight. Default=1
            start (int): number which represent a start position (nest)
            end (int): number which represent end position (food)
        Example:
            ant_colony = AntColony(german_distances, 100, 20, 2000, 0.95, alpha=1, beta=2)
        """
        self.distances = distances
        if pheromone == []:
            self.pheromone = np.ones(self.distances.shape) / len(distances)
        else:
            self.pheromone = pheromone
        self.all_inds = range(len(distances))
        self.n_ants = n_ants
        self.n_iterations = n_iterations
        self.decay = decay
        self.alpha = alpha
        self.beta = beta


    def run(self, start_num, end_num):
        """
        Args:
            start_num (int): number which represent a start position (nest)
            end_num (int): number which represent end position (food)
            """
        self.start_num = start_num
        self.end_num = end_num
        shortest_path = None
        all_time_shortest_path = ("placeholder", np.inf)
        for i in range(self.n_iterations):
            all_paths = self.gen_all_paths() #here we generate all paths from all ants
            self.pheromone *= self.decay
            self.spread_pheronome(all_paths)
            shortest_path = min(all_paths, key=lambda x: x[1])
            #print(shortest_path)
            if shortest_path[1] < all_time_shortest_path[1]:
                all_time_shortest_path = shortest_path
        return all_time_shortest_path

    def update_pheromone(self):
        self.pheromone *= self.decay

    def run_reducer(self, start_num, end_num):
        """
                Args:
                    start_num (int): number which represent a start position (nest)
                    end_num (int): number which represent end position (food)
        """
        self.start_num = start_num
        self.end_num = end_num
        for i in range(self.n_iterations):
            all_paths = self.gen_all_paths()  # here we generate all paths from all ants
            self.spread_pheronome_reducer(all_paths)
        return self.pheromone


    def gen_all_paths(self):
        all_paths = []
        for i in range(self.n_ants):
            path = self.gen_path()
            all_paths.append((path, self.gen_path_dist(path)))
        return all_paths

    def gen_path(self):
        path = []
        visited = set()
        visited.add(self.start_num)
        prev = self.start_num
        for i in range(len(self.distances) - 1):
            move = self.pick_move(self.pheromone[prev], self.distances[prev], visited)
            path.append((prev, move))
            prev = move
            visited.add(move)
            if move == self.end_num:
                break
        return path

    def spread_pheronome(self, all_paths):
        sorted_paths = sorted(all_paths, key=lambda x: x[1])
        for path, dist in sorted_paths:
            for move in path:
                self.pheromone[move] += 1.0 / self.distances[move]

    def spread_pheronome_reducer(self, all_paths):
        sorted_paths = sorted(all_paths, key=lambda x: x[1])
        self.pheromone = np.zeros(self.pheromone.shape)
        for path, dist in sorted_paths:
            for move in path:
                self.pheromone[move] += 1.0 / self.distances[move]

    def gen_path_dist(self, path):
        total_dist = 0
        for ele in path:
            total_dist += self.distances[ele]
        return total_dist


    def pick_move(self, pheromone, dist, visited):
        pheromone = np.copy(pheromone)
        pheromone[list(visited)] = 0

        row = pheromone ** self.alpha * (( 1.0 / dist) ** self.beta)
        norm_row = row / row.sum()
        move = np_choice(self.all_inds, 1, p=norm_row)[0]
        return move