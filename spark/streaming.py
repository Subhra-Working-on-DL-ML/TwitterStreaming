from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json, udf
from pyspark.sql.types import StructType, StringType, DoubleType
from elasticsearch import Elasticsearch

spark = (SparkSession.builder.appName("TwitterSparkES")
         .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.1")
         .getOrCreate())

schema = StructType().add("id", StringType()).add("text", StringType()).add("created_at", StringType())

df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "twitter_stream") \
    .load()

parsed = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json("value", schema).alias("tweet")) \
    .select("tweet.*")

def to_es(batch_df, _):
    es = Elasticsearch("http://localhost:9200")
    for row in batch_df.collect():
        es.index(index="tweets", document=row.asDict())

parsed.writeStream.outputMode("append").foreachBatch(to_es).start().awaitTermination()
