# Ant Colony Optimization
## Apache Hadoop & Apache Spark
### Task:
> Optymalizajca: algorytm mrowkowy

>Rozpoznać srodowiska Apache Hadoop oraz Apache Spark i zrealizować w nich równoległy algorytm mrowkowy
ACO (http://atol.am.gdynia.pl/~tomera/publikacje/PTETiS_2015a_Tomera.pdf) do wyznaczania  rutingu  pakietów  w  sieciach  komputerowych. Rozważyć  dwa przykłady  sieci  (mniej  i  bardziej  złożone).  Ocenić  wpływ  zrównoleglenia  na 
szybkość  algorytmu. Przedstawić  graficznie  zbieżność  obu  algorytmów  w  wersji sekwencyjnej – wartości funkcji celu w kolejnych iteracjach.


### How to start (Ubuntu)
1. Install java: 
```
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update
sudo apt-get install oracle-java8-installer
```
2. Install Apache Hadoop
```
wget https://www-us.apache.org/dist/hadoop/common/hadoop-2.8.5/hadoop-2.8.5.tar.gz
tar -xzvf hadoop-2.8.5.tar.gz
sudo mv hadoop-2.8.5 /usr/local/hadoop
```
3. Install ssh server
```
apt-get install openssh-server
/etc/init.d/ssh restart
```
4. Create user for hadoop
```
useradd hadoop 
passwd hadoop 
su hadoop
```
5. Generate ssh key
```
ssh-keygen -t rsa 
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys 
chmod 0600 ~/.ssh/authorized_keys 
```
6. Add environment variables
```
export HADOOP_HOME=/usr/local/hadoop 
export HADOOP_MAPRED_HOME=$HADOOP_HOME 
export HADOOP_COMMON_HOME=$HADOOP_HOME 
export HADOOP_HDFS_HOME=$HADOOP_HOME 
export YARN_HOME=$HADOOP_HOME 
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native 
export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin 
export HADOOP_INSTALL=$HADOOP_HOME

source ~/.bashrc
```
7. Configure hadoop
```
cd $HADOOP_HOME/etc/hadoop
```
* *hadoop-env.sh* - hadoop environment variables
```
export JAVA_HOME=/usr/lib/jvm/java-8-oracle
```
* *core-site.xml* - information such as the port number used for Hadoop instance, memory allocated for the file system, memory limit for storing the data, and size of Read/Write buffers.
```
<configuration>

   <property>
      <name>fs.default.name</name>
      <value>hdfs://localhost:9000</value> 
   </property>
 
</configuration>
```
* *hdfs-site.xml* - information such as the value of replication data, namenode path, and datanode paths of your local file systems. It means the place where you want to store the Hadoop infrastructure.
```
<configuration>

   <property>
      <name>dfs.replication</name>
      <value>1</value>
   </property>
    
   <property>
      <name>dfs.name.dir</name>
      <value>file:///home/hadoop/hadoopinfra/hdfs/namenode </value>
   </property>
    
   <property>
      <name>dfs.data.dir</name> 
      <value>file:///home/hadoop/hadoopinfra/hdfs/datanode </value> 
   </property>
       
</configuration>
```
* *yarn-site.xml* - configure yarn into Hadoop (framework for job sheduling and cluster resource management)
```
<configuration>
 
   <property>
      <name>yarn.nodemanager.aux-services</name>
      <value>mapreduce_shuffle</value> 
   </property>
  
</configuration>
```
* *mapred-site.xml* - which MapReduce framework we are using

`cp mapred-site.xml.template mapred-site.xml `
```
<configuration>
 
   <property> 
      <name>mapreduce.framework.name</name>
      <value>yarn</value>
   </property>
   
</configuration>
```
8. Verify installation
```
cd ~ 
hdfs namenode -format 
start-all.sh
```
Hadoop services: http://localhost:50070/

Hadoop cluster: http://localhost:8088/
