import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as F
from pyspark.sql.functions import col, year, month, dayofmonth

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init("trusted_to_refined", getResolvedOptions(sys.argv, ['JOB_NAME']))

# Definir caminho das camadas
s3_trusted_path = "s3://datalake-bruno-s-pb/Trusted/"
s3_refined_path_full = "s3://datalake-bruno-s-pb/Refined/full/"
s3_refined_path_fato_filmes = "s3://datalake-bruno-s-pb/Refined/fato_filmes/"
s3_refined_path_filme = "s3://datalake-bruno-s-pb/Refined/filme/"
s3_refined_path_genero = "s3://datalake-bruno-s-pb/Refined/genero/"
s3_refined_path_idioma = "s3://datalake-bruno-s-pb/Refined/idioma/"
s3_refined_path_elenco = "s3://datalake-bruno-s-pb/Refined/elenco/"
s3_refined_path_produtora = "s3://datalake-bruno-s-pb/Refined/produtora/"
s3_refined_path_tempo = "s3://datalake-bruno-s-pb/Refined/tempo/"

# Função para adicionar as colunas de data (ano, mês, dia)
def add_year_month_day(df, date_column):
    return df.withColumn('ano', year(F.col(date_column))) \
             .withColumn('mes', month(F.col(date_column))) \
             .withColumn('dia', dayofmonth(F.col(date_column)))

# Ler os dados da camada trusted
df_tmdb = spark.read.parquet(f"{s3_trusted_path}TMDB/Parquet/2025/03/04/") \
    .select(
        "id",
        "tituloPrincipal",
        "tituloOriginal",
        "anoLancamento",
        "tempoMinutos",
        "genero", 
        "notaMedia",
        "numeroVotos",  
        "sinopse",  
        "idiomas",  
        "elenco",  
        "orcamento",  
        "receita",  
        "produtoras" 
    )

# Criação da tabela Fato Filmes
df_fato_filmes = df_tmdb.select(
    'id',
    F.col('id').alias('id_filme'),
    F.monotonically_increasing_id().alias('id_genero'),  
    F.monotonically_increasing_id().alias('id_idioma'),  
    F.monotonically_increasing_id().alias('id_artista'),  
    F.monotonically_increasing_id().alias('id_produtora'),  
    F.monotonically_increasing_id().alias('id_tempo'),  
    'numeroVotos', 
    'orcamento',
    'receita',
    'anoLancamento'
)

# Criação da Dimensão Filme
df_filme = df_tmdb.select(
    F.col('id').alias('id_filme'),
    'tituloPrincipal',
    'tituloOriginal',
    'tempoMinutos',
    'anoLancamento',
    'sinopse'
)

# Criação da Dimensão Gênero
df_genero = df_tmdb.select(
    F.explode('genero').alias('genero')
).distinct().withColumn('id_genero', F.monotonically_increasing_id())

# Criação da Dimensão Idioma
df_idioma = df_tmdb.select(
    F.explode('idiomas').alias('idioma')
).distinct().withColumn('id_idioma', F.monotonically_increasing_id())

# Criação da Dimensão Elenco
df_elenco = df_tmdb.select(
    F.explode('elenco').alias('elenco')
).distinct().withColumn('id_artista', F.monotonically_increasing_id())

# Criação da Dimensão Produtora
df_produtora = df_tmdb.select(
    F.explode('produtoras').alias('produtora')
).distinct().withColumn('id_produtora', F.monotonically_increasing_id())

# Criação da Dimensão Tempo (adicionando ano, mês, dia)
df_tempo = add_year_month_day(df_tmdb, 'anoLancamento') \
    .select('ano', 'mes', 'dia') \
    .withColumn('id_tempo', F.monotonically_increasing_id())

# Escrever os DataFrames nas camadas refinadas
df_tmdb.write.parquet(s3_refined_path_full, mode='overwrite')
df_fato_filmes.write.parquet(s3_refined_path_fato_filmes, mode='overwrite')
df_filme.write.parquet(s3_refined_path_filme, mode='overwrite')
df_genero.write.parquet(s3_refined_path_genero, mode='overwrite')
df_idioma.write.parquet(s3_refined_path_idioma, mode='overwrite')
df_produtora.write.parquet(s3_refined_path_produtora, mode='overwrite')
df_tempo.write.parquet(s3_refined_path_tempo, mode='overwrite')

# Finalizar o trabalho
job.commit()
