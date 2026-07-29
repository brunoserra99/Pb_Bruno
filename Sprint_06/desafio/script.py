import boto3
import os
from datetime import datetime
from dotenv import load_dotenv

# Credenciais AWS
load_dotenv()

# Configuração do cliente S3
s3 = boto3.client('s3',
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'], 
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'], 
    aws_session_token=os.environ['AWS_SESSION_TOKEN'],
    region_name='us-east-1'
)
 
# Nome do bucket
bucket_name = 'datalake-bruno-s-pb' 

# Caminho local dos arquivos
file_path_movie = '/desafio/movies.csv'
file_path_series = '/desafio/series.csv'

year = datetime.now().strftime('%Y')
month = datetime.now().strftime('%m')
day = datetime.now().strftime('%d')


# Nomes no S3
file_name_movie = f'Raw/Local/CSV/Movies/{year}/{month}/{day}/movies.csv'
file_name_series = f'Raw/Local/CSV/Series/{year}/{month}/{day}/series.csv'



# Função para upload dos arquivos
def upload_file(file_path, file_name):
    s3.upload_file(file_path, bucket_name, file_name)
    print(f"Arquivo {file_path} enviado para {file_name}.")


# Enviar filmes e séries
upload_file(file_path_movie, file_name_movie)
upload_file(file_path_series, file_name_series)

