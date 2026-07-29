import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType, ArrayType

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Esquema para estrutura do JSON
esquema_json = StructType([
    StructField("id", StringType(), True),
    StructField("tituloPrincipal", StringType(), True),
    StructField("tituloOriginal", StringType(), True),
    StructField("anoLancamento", StringType(), True),
    StructField("tempoMinutos", IntegerType(), True),
    StructField("genero", ArrayType(StringType()), True),
    StructField("notaMedia", FloatType(), True),
    StructField("numeroVotos", IntegerType(), True),
    StructField("sinopse", StringType(), True),
    StructField("idiomas", ArrayType(StringType()), True),
    StructField("elenco", ArrayType(StringType()), True),
    StructField("orcamento", IntegerType(), True),
    StructField("receita", IntegerType(), True),
    StructField("produtoras", ArrayType(StringType()), True)
])

input_path = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

# Lendo o arquivo JSON
dataframe_json = spark.read.option("multiline", "true").json(input_path, schema=esquema_json)

# Substituindo valores 
dataframe_json = dataframe_json.replace("\\N", None)
dataframe_json = dataframe_json.na.drop()

# Filtrando dados 
dataframe_json = dataframe_json.filter(
    (col("orcamento") > 0) & 
    (col("receita") > 0) & 
    (col("anoLancamento") != '') & 
    (col("tituloPrincipal") != '') & 
    (col("id") != '')
)

# Salvando os dados processados em formato Parquet
dataframe_json.write.mode("overwrite").parquet(target_path)

job.commit()


