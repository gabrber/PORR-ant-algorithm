#!/usr/bin/env bash

outNum=501
inputFilename="inp.txt"
mainCommand='hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.8.5.jar -mapper "python $PWD/mapper2.py" -reducer "python $PWD/reducer2.py" -input "/porr/$inputFilename" -output "/porr/output_porr$outNum"'
eval $mainCommand
