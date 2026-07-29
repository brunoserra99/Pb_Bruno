import boto3
import pandas as pd
import script_up as upload


# Baixar o arquivo do S3
upload.s3.download_file(upload.bucket_name, upload.file_name, upload.download_path)
print(f"Arquivo {upload.download_path} baixado com sucesso.")

# Carregar os dados do CSV
#dados = pd.read_csv(file_name)

# Carregar os dados do CSV
arquivo_base ='Sprint_05/desafio/corridas_7_dias_manipulado.csv'
dados = pd.read_csv(arquivo_base)

# Tratar valores ausentes
dados['km_total'] = dados['km_total'].fillna(0)
dados['valor_corrida'] = dados['valor_corrida'].fillna(0)
dados['data_abertura'] = dados['data_abertura'].fillna('1000-01-01')

# Clausula que filtra dados usando ao menos dois operadores logicos
filtro = dados[(dados['status'] == 'CONCLUÍDA') & (dados['km_total'] > 5)].copy()

# Duas funcoes de agregacao: media/soma
media_km = filtro['km_total'].mean()
soma_valor = filtro['valor_corrida'].sum()

# Uma funcao condicional: indica se a corrida foi longa sim/nao
filtro['corrida_longa'] = filtro['km_total'].apply(lambda x: 'Sim' if x > 10 else 'Não')

# Uma funcao de conversão: Converter para datetime
filtro['data_abertura'] = pd.to_datetime(filtro['data_abertura'])

# Uma funcao de data: extrair o mes
filtro['mes_abertura'] = filtro['data_abertura'].dt.day

# Uma funcao de string: manipular a coluna
filtro['origem_cidade_upper'] = filtro['origem_cidade'].str.upper()

# Resultado
print(f"Média de KM Total (filtrados): {media_km}")
print(f"Soma do Valor Corrida (filtrados): {soma_valor}")
print(filtro[['km_total', 'corrida_longa', 'data_abertura', 'mes_abertura', 'origem_cidade_upper', 'veiculo_placa']].head(10))

#print(filtro[['km_total', 'corrida_longa', 'data_abertura', 'mes_abertura', 'origem_cidade_upper']].sort_values(by='km_total', ascending=True).head(10))

# Salvar os dados manipulados em arquivo CSV
filtro.to_csv('Sprint_05/desafio/corridas_7_dias_manipulado.csv', index=False)
print('Arquivo manipulado salvo como Sprint_05/desafio/corridas_7_dias_manipulado.csv')

# Fazer o upload do arquivo manipulado para o S3
upload.s3.upload_file('Sprint_05/desafio/corridas_7_dias_manipulado.csv', upload.bucket_name, 'corridas_7_dias_manipulado.csv')

