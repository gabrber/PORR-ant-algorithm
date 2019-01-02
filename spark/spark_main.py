# spark
from pyspark import SparkConf
from pyspark import SparkContext

# ACO code
import json
import ast

import numpy as np
from random import randrange
from aco_algorithm import AntColony

# spark config
conf = SparkConf()
conf.setMaster('spark://52120768ea4b:7077')
conf.setAppName('spark-basic')
sc = SparkContext(conf=conf)

# read data
json_file = open('/home/PORR-ant-algorithm/spark/files/input.txt')
json_str = json_file.read()
json_data = json.loads(json_str)

distances = np.asarray(json_data['distances'])
pheromone = np.ones(distances.shape) / len(distances)

# ant colony object
ant_colony = AntColony(distances, json_data['n_ants'], json_data['n_iterations'], json_data['decay'], pheromone, json_data['alpha'], json_data['beta'])

# number of parallel nodes
no_parallel_instances = sc.parallelize(range(100))

# run
res = no_parallel_instances.map(lambda row: ant_colony.run(0, 5))
#res = no_parallel_instances.map(lambda row: simulate(row))
collected = res.collect()
print(collected)
for i in collected:
    print(i)
print(res.count())
print("finished")