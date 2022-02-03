# Source code from https://github.com/jleetutorial/python-spark-tutorial


from pyspark import SparkContext, SparkConf

if __name__ == "__main__":
    # Setup: Run the application on an embedded spark instance on the machine. 
    # This can use up to 3/4 of the CPU.
    conf = SparkConf().setAppName("word count").setMaster("local[3]")
    
    # 1. Crate spark context. We imported this from Spark API. 
    # This is the entry point to Spark Core.
    sc = SparkContext(conf = conf)  
    
    # Load dataset. RDD: Resilient Distributed Dataset
    lines = sc.textFile("in/word_count.text") 
    
    words = lines.flatMap(lambda line: line.split(" "))
    
    wordCounts = words.countByValue()
    
    for word, count in wordCounts.items():
        print("{} : {}".format(word, count))
