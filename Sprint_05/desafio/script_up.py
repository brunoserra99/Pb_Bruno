import boto3

chave = 'ID-Chave'
chave_secreta = 'Id-chaves'
token = 'Id-chaves'

# Nome do bucket e do arquivo
bucket_name = 'bucketbmseaws'
file_path = 'Sprint_05/desafio/corridas_7_dias.csv'
file_name = 'corridas_7_dias.csv'

download_path = 'Sprint_05/desafio/corridas_7_dias_manipulado.csv'
# Configuração do cliente S3
s3 = boto3.client('s3',
    aws_access_key_id=chave, 
    aws_secret_access_key=chave_secreta, 
    aws_session_token=token,
    region_name='us-east-1'
    )               

# Upload do arquivo para o S3
s3.create_bucket(
    Bucket=bucket_name
    )


s3.upload_file(file_path, bucket_name, file_name)
print(f"Arquivo {file_name} enviado com sucesso para o bucket {bucket_name}.")
