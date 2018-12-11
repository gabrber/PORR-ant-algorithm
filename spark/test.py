# spark-basic.py
from pyspark import SparkConf
from pyspark import SparkContext

conf = SparkConf()
conf.setMaster('spark://gabriela-TM1703:7077')
conf.setAppName('spark-basic')
sc = SparkContext(conf=conf)

# ACO code
import numpy as np
from random import randrange
from aco_algorithm import AntColony

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

ant_colony = AntColony(rand_dist, 20, 100, 0.95, alpha=1, beta=1)
shortest_path = ant_colony.run(0, 5)

print("--- Final result is: ---")
print(shortest_path)
