import os

for i in range(1):

    os.system('hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.8.5.jar \
    -file mapreduce/mapper.py \
    -mapper mapper.py \
    -file mapreduce/reducer.py \
    -reducer reducer.py \
    -input mapreduce/input.txt \
    -output mapreduce/output')
