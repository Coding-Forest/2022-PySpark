# <span id='top'>01 Basics - Apache Spark</span>

<br>

[[Install]](#install)  

<br>

## <span id='install'>Install</span>

[[Top]](#top)

<br>

Requirements:
- `java`: apache runs on java. 
- `python spark`

<br>

`java`

1. Path configuration 

        nano .bashrc
    
            export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64  <------ ADD THIS
            export PATH=$PATH:$JAVA_HOME/bin                    <------ ADD BINARY


- Add binary of java runtime environment to the path. This enables the use of java commands from the command line. 

<br>

`Spark`

1. Download

- Choose your version here at: https://spark.apache.org/downloads.html
- download 
  - `tgz` file from the link https://www.apache.org/dyn/closer.lua/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz
  - or `wget https://www.apache.org/dyn/closer.lua/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz`

 
2. Unzip and  install 

Create a folder where we unzip `spark`. Usually on Linux, software that don't come with a distribution should be stored in `/opt/`

    sudo mkdir /opt/apache-spark     <------ located inside opt folder. 

Then `tar` the `apache-spark` file in the `/opt/` directory. 

    sudo tar xvzf spark-3.1.2-bin-hadoop3.2.tgz -C /opt/apache-spark

Edit `.bashrc` 

    cd /opt/apache-spark

    pwd
    /opt/apache-spark/spark-3.1.2-bin-hadoop3.2


    nano .bashrc

    export SPARK_HOME=/opt/apache-spark/spark-3.1.2-bin-hadoop3.2 <--- Add this
    export PATH=$PATH:$JAVA_HOME/bin:$SPARK_HOME/bin            <----- Update PATH


`Source` it to apply the changes.

    source ~/.bashrc

<br>

3. Start a `pyspark` session 

- Test-run `PySpark` to verify installation result. 

    pyspark

    2022-02-02 18:22:26,064 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
    Setting default log level to "WARN".
    To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
    Welcome to
            ____              __
           / __/__  ___ _____/ /__
          _\ \/ _ \/ _ `/ __/  '_/
         /__ / .__/\_,_/_/ /_/\_\   version 3.1.2
            /_/

    Using Python version 3.8.10 (default, Nov 26 2021 20:14:08)
    Spark context Web UI available at http://codingforest:4040
    Spark context available as 'sc' (master = local[*], app id = local-1643793763311).
    SparkSession available as 'spark'.