import json
import requests
import boto3
from datetime import datetime

def lambda_handler(event, context):
    client = boto3.client('s3',
        aws_access_key_id='id_XXXX', 
        aws_secret_access_key='id_XXXX', #credenciais alteradas para o envio ao repositorio.
        aws_session_token='id_XXXX',
        region_name='us-east-1'
    )
    
    year = datetime.now().strftime('%Y')
    month = datetime.now().strftime('%m')
    day = datetime.now().strftime('%d')
    bucket_name = 'datalake-bruno-s-pb'
    #s3_path = f'Raw/TMDB/JSON/{year}/{month}/{day}/'
    s3_path = f'Raw/TMDB/JSON/teste/{year}/{month}/{day}/'

    chave_api_tmdb = 'id_XXXX' #credenciais alteradas para o envio ao repositorio.
    
    def buscar_filmes(pagina=1):
        url = f"https://api.themoviedb.org/3/discover/movie?api_key={chave_api_tmdb}&primary_release_date.gte=2015-01-01&page={pagina}&language=pt-BR&with_genres=18,10749"
        resposta = requests.get(url)
        return resposta.json()

    def obter_id_imdb(tmdb_id):
        url = f"https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={chave_api_tmdb}&append_to_response=external_ids"
        resposta = requests.get(url)
        detalhes = resposta.json()
        return detalhes.get('external_ids', {}).get('imdb_id', None)

    def salvar_filmes(dados, prefixo_arquivo, limite=100, indice=1):
        lista_filmes = []
        for filme in dados['results']:
            url_detalhes = f"https://api.themoviedb.org/3/movie/{filme['id']}?api_key={chave_api_tmdb}&language=pt-BR"
            resposta_detalhes = requests.get(url_detalhes)
            detalhes_filme = resposta_detalhes.json()
            
            id_imdb = obter_id_imdb(filme['id'])

            info_filme = {
                'id': id_imdb,
                'titulo': filme['title'],
                'data_lancamento': filme['release_date'],
                'orcamento': detalhes_filme.get('budget', 0),  
                'receita': detalhes_filme.get('revenue', 0),  
                'produtoras': [p['name'] for p in detalhes_filme.get('production_companies', [])] 
            }
            lista_filmes.append(info_filme)

        for i in range(0, len(lista_filmes), limite):
            nome_arquivo = f"{prefixo_arquivo}_parte_{indice}.json"
            indice += 1

            client.put_object(Body=json.dumps(lista_filmes[i:i+limite], ensure_ascii=False, indent=4), 
                            Bucket=bucket_name, 
                            Key=f'{s3_path}{nome_arquivo}')
            print(f'Arquivo {nome_arquivo} carregado para o S3 em {s3_path}')

        return indice


    def obter_elenco(filme_id):
        url = f"https://api.themoviedb.org/3/movie/{filme_id}/credits?api_key={chave_api_tmdb}&language=pt-BR"
        resposta = requests.get(url)
        return resposta.json()

    pagina = 1
    indice_arquivo = 1
    filmes_total = []

    while True:
        dados = buscar_filmes(pagina)
        if not dados or 'results' not in dados or not dados['results']:
            break

        filmes_total.extend(dados['results'])

        if len(filmes_total) >= 100:
            indice_arquivo = salvar_filmes({'results': filmes_total}, 'filmes', limite=100, indice=indice_arquivo)
            filmes_total = []

        pagina += 1

    if filmes_total:
        salvar_filmes({'results': filmes_total}, 'filmes', limite=100, indice=indice_arquivo)

    return {
        'statusCode': 200,
        'body': json.dumps('Arquivos carregados no S3 com sucesso!')
    }
