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
