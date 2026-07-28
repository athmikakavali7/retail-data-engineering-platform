from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("RetailOrderStreaming")
    .master("spark://localhost:7077")
    .config(
        "spark.jars.packages",
        "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.2"
    )
    .getOrCreate()
)

spark.sparkContext.setLogLevel("WARN")

kafka_df = (
    spark.readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", "localhost:9092")
    .option("subscribe", "orders")
    .option("startingOffsets", "earliest")
    .load()
)

kafka_df.printSchema()

query = (
    kafka_df.writeStream
    .format("console")
    .outputMode("append")
    .start()
)

query.awaitTermination()