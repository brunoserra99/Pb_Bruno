import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, split, year, month, dayofmonth


sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init("trusted_to_refined", getResolvedOptions(sys.argv, ['JOB_NAME']))

# Definir caminho das camadas
s3_trusted_path = "s3://datalake-bruno-s-pb/Trusted/"
s3_refined_path_fato_filmes = "s3://datalake-bruno-s-pb/Refined/fato_filmes/"
s3_refined_path_dim_filme = "s3://datalake-bruno-s-pb/Refined/dim_filme/"
s3_refined_path_dim_filme_artista = "s3://datalake-bruno-s-pb/Refined/dim_filme_artista/"
s3_refined_path_dim_artista = "s3://datalake-bruno-s-pb/Refined/dim_artista/"
s3_refined_path_dim_data_lancamento = "s3://datalake-bruno-s-pb/Refined/dim_data_lancamento/"
s3_refined_path_dim_produtora = "s3://datalake-bruno-s-pb/Refined/dim_produtora/"

# Ler os dados da camada trusted
df_local = spark.read.parquet(f"{s3_trusted_path}Local/Parquet/Movies/")
df_tmdb = spark.read.parquet(f"{s3_trusted_path}TMDB/Parquet/2025/02/03/")

# Unir os DataFrames df_local e df_tmdb
df_merged = df_local.join(df_tmdb, df_local.id == df_tmdb.id, 'full') \
    .select(
        df_local.id.alias('id_filme'),
        df_tmdb.orcamento,
        df_tmdb.receita,
        df_local.notaMedia,
        df_local.numeroVotos,
        df_local.tituloPrincipal,  
        df_local.anoLancamento,
        df_local.genero,
        df_local.tempoMinutos,
        df_local.generoArtista,
        df_local.personagem,
        df_local.nomeArtista,
        df_local.anoNascimento,
        df_local.anoFalecimento,
        df_local.profissao,
        df_local.titulosMaisConhecidos,
        df_tmdb.data_lancamento,
        df_tmdb.produtoras
    )

# Criação da tabela Fato Filmes
df_fato_filmes = df_merged.select(
    'id_filme',
    'orcamento',
    'receita',
    'notaMedia',
    'numeroVotos'
)

# Criação da Dimensão Filme
df_dim_filme = df_merged.select(
    'id_filme',
    'tituloPrincipal',  
    'anoLancamento',
    'genero',
    'tempoMinutos'
)

# Criação da Dimensão Filme Artista
df_dim_filme_artista = df_merged.select(
    'id_filme',
    'nomeArtista',
    'personagem'
) \
    .withColumnRenamed('nomeArtista', 'id_artista') \
    .withColumnRenamed('personagem', 'papel')

# Criação da Dimensão Artista
df_dim_artista = df_merged.select(
    'nomeArtista',
    'generoArtista',
    'anoNascimento',
    'anoFalecimento'
) \
    .withColumnRenamed('nomeArtista', 'id_artista') \
    .withColumnRenamed('generoArtista', 'genero') \
    .withColumnRenamed('anoNascimento', 'ano_nascimento') \
    .withColumnRenamed('anoFalecimento', 'ano_falecimento')

# Criação da Dimensão Tempo
df_dim_data_lancamento = df_merged.select(
    'data_lancamento'
) \
    .withColumn('id_tempo', col('data_lancamento')) \
    .withColumn('ano', year(col('data_lancamento'))) \
    .withColumn('mes', month(col('data_lancamento'))) \
    .withColumn('dia', dayofmonth(col('data_lancamento')))

# Criação da Dimensão Produtora
df_dim_produtora = df_merged.select(
    'produtoras'
) \
    .withColumnRenamed('produtoras', 'id_produtora')

# Escrever os DataFrames nas camadas refinadas
df_fato_filmes.write.parquet(s3_refined_path_fato_filmes, mode='overwrite')
df_dim_filme.write.parquet(s3_refined_path_dim_filme, mode='overwrite')
df_dim_filme_artista.write.parquet(s3_refined_path_dim_filme_artista, mode='overwrite')
df_dim_artista.write.parquet(s3_refined_path_dim_artista, mode='overwrite')
df_dim_data_lancamento.write.parquet(s3_refined_path_dim_data_lancamento, mode='overwrite')
df_dim_produtora.write.parquet(s3_refined_path_dim_produtora, mode='overwrite')

# Finalizar o trabalho
job.commit()
