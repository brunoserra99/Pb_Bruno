import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, upper, desc, count
from pyspark.sql.types import StructType, StructField, StringType, IntegerType


## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME','S3_INPUT_PATH','S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

dados = spark.read.csv(source_file, header=True, inferSchema=True)

dados.printSchema()

dados = dados.withColumn("nome", upper(col("nome")))

print(f"Linhas: {dados.count()}")

agrupados = dados.groupBy("ano", "sexo").agg(count("nome").alias("total"))
agrupados.orderBy(desc("ano")).show()

fem_top = dados.filter(col("sexo") == "F").orderBy(desc("total")).select("nome", "total", "ano").first()
print(f"Feminino com mais registros: {fem_top['nome']} ({fem_top['ano']})")

masc_top = dados.filter(col("sexo") == "M").orderBy(desc("total")).select("nome", "total", "ano").first()
print(f"Masculino com mais registros: {masc_top['nome']} ({masc_top['ano']})")

totais_ano = dados.groupBy("ano").agg(count("*").alias("registros")).orderBy("ano").limit(10)
totais_ano.show()


dados.write.partitionBy("sexo", "ano") \
    .mode("overwrite") \
    .json(target_path)



job.commit()