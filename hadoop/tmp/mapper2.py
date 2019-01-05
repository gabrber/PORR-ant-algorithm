#!/usr/bin/env python
"""mapper.py"""
import sys
import math
import json

batch_size = 100 #this is the size of every iteration

for line in sys.stdin:
    line = line.strip()
    dic = line
    dic = json.loads(dic) #we make dictionary from string

    all_ants = float(dic['n_ants'])

    upper_bond = int(math.ceil(all_ants/batch_size))

    for splits_number in range(upper_bond):
        if batch_size*(1+splits_number) < all_ants:
            dic['n_ants'] = batch_size
            dic['n_best'] = dic['n_ants']
        else:
            dic['n_ants'] = int(all_ants - splits_number*batch_size)
            dic['n_best'] = dic['n_ants']
        print('%s\t%s' % (splits_number, json.dumps(dic)))
