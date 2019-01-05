#!/usr/bin/env bash

outNum=1
inputFilename="input500_10_800.txt"
mainCommand='hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.8.5.jar -mapper "python $PWD/mapper.py" -reducer "python $PWD/reducer.py" -input "/porr/$inputFilename" -output "/porr/output_porr$outNum"'
eval $mainCommand
