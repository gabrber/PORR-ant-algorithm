#!/usr/bin/env bash

outNum=450
inputFilename="inp.txt"
for ((i=1;$i<=3;i++)); do
    putCommand='hadoop fs -put -f ./$inputFilename /porr/$inputFilename'
    eval $putCommand
    mainCommand='hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.8.5.jar -mapper "python $PWD/mapper.py" -reducer "python $PWD/reducer.py" -input "/porr/$inputFilename" -output "/porr/output_porr$outNum"'
    eval $mainCommand
    copyCommand='hadoop fs -get -f /porr/output_porr$outNum/part-00000 ./'
    eval $copyCommand
    pheromoneUpdate='./update_pheromone.py "part-00000" "$inputFilename"'
    eval $pheromoneUpdate
    putCommand='hadoop fs -put -f ./$inputFilename /porr/$inputFilename'
    eval $putCommand
    outNum=$((outNum+1))
done
finalOutput='./final_output.py "part-00000" "$inputFilename"'
eval $finalOutput