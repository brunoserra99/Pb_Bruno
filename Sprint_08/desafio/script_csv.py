import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType

esquema_csv_movies = StructType([
    StructField("id", StringType(), True),
    StructField("tituloPincipal", StringType(), True),
    StructField("tituloOriginal", StringType(), True),
    StructField("anoLancamento", IntegerType(), True),
    StructField("tempoMinutos", IntegerType(), True),
    StructField("genero", StringType(), True),
    StructField("notaMedia", FloatType(), True),
    StructField("numeroVotos", IntegerType(), True),
    StructField("generoArtista", StringType(), True),
    StructField("personagem", StringType(), True),
    StructField("nomeArtista", StringType(), True),
    StructField("anoNascimento", IntegerType(), True),
    StructField("anoFalecimento", IntegerType(), True),
    StructField("profissao", StringType(), True),
    StructField("titulosMaisConhecidos", StringType(), True) ])

input_path = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']
dataframe_movies = spark.read.option("delimiter", "|").option("header", "false").schema(esquema_csv_movies).csv(input_path)

dataframe_movies = dataframe_movies.replace("\\N", None)
dataframe_movies = dataframe_movies.na.drop()
dataframe_movies = dataframe_movies.filter(  (col("notaMedia") > 0) & (col("numeroVotos") > 0) & (col("anoNascimento") > 0) & (col("anoFalecimento") > 0) & (col("anoLancamento") > 0) & (col("tempoMinutos") > 0) )

dataframe_movies = dataframe_movies.withColumnRenamed("tituloPincipal", "tituloPrincipal")
dataframe_movies.write.mode("overwrite").parquet(target_path)

job.commit()