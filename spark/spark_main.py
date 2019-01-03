# spark
from pyspark import SparkConf
from pyspark import SparkContext

# ACO code
import json
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
pheromones = np.asarray(json_data['pheromones'])

# ant colony object
ant_colony = AntColony(distances, json_data['n_ants'], json_data['n_iterations'], json_data['decay'], pheromones, json_data['alpha'], json_data['beta'])

# SPARK
# number of parallel runs
no_parallel_instances = sc.parallelize(range(2))

# run
parallel_runs = no_parallel_instances.map(lambda row: ant_colony.run_get_pheromone(json_data['start_point'], json_data['end_point']))
add_pheromone = parallel_runs.reduce(lambda a, b: a + b)

# get results and update pheromone
collected = parallel_runs.collect()
parallel_runs.count()

pheromones += add_pheromone
#print(add_pheromone)

# final ACO
ant_colony_final = AntColony(distances, json_data['n_ants'], 1, json_data['decay'], pheromones, json_data['alpha'], json_data['beta'])
shortest_path = ant_colony_final.run(json_data['start_point'], json_data['end_point'])

print("***********************")
print(shortest_path)
print("***********************")