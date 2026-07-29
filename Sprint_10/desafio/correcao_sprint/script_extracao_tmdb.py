import json
import requests
import boto3
from datetime import datetime

def lambda_handler(event, context):
    # Criação do cliente do S3
    client = boto3.client('s3',
        aws_access_key_id="id_xxx", 
        aws_secret_access_key="id_xxx",
        aws_session_token="id_xxx",
        region_name='us-east-1'
    )

    # Definindo data atual para caminho no S3
    year = datetime.now().strftime('%Y')
    month = datetime.now().strftime('%m')
    day = datetime.now().strftime('%d')
    bucket_name = 'datalake-bruno-s-pb'
    s3_path = f'Raw/TMDB/JSON/{year}/{month}/{day}/'

    # Chave de API do TMDB
    chave_api_tmdb = 'id_xxx'

    # Lista de filmes para buscar informações
    filmes = ["Rocky", "Rocky II", "Rocky III", "Rocky IV", "Rocky V", "Rocky 6"]
    
    # Dados de filmes
    filmes_dados = []

    # Obtendo informações de cada filme da TMDb
    for filme in filmes:
        url = f'https://api.themoviedb.org/3/search/movie'
        params = {
            'api_key': chave_api_tmdb,
            'query': filme
        }

        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            if data['results']:
                movie_info = data['results'][0]
                movie_id = movie_info['id']
                
                # Endpoint para obter detalhes do filme
                movie_details_url = f'https://api.themoviedb.org/3/movie/{movie_id}'
                movie_details_response = requests.get(movie_details_url, params={'api_key': chave_api_tmdb})
                
                if movie_details_response.status_code == 200:
                    movie_details = movie_details_response.json()

                    # Obter detalhes do elenco
                    credits_url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits'
                    credits_response = requests.get(credits_url, params={'api_key': chave_api_tmdb})

                    elenco = []
                    if credits_response.status_code == 200:
                        credits_data = credits_response.json()

                        # Filtrando apenas atores principais
                        for cast_member in credits_data.get('cast', []):
                            if cast_member.get('character') in ["Rocky Balboa", "Apollo Creed", "Clubber Lang"]:  # Exemplo de personagens principais
                                elenco.append({
                                    'nomeArtista': cast_member.get('name'),
                                    'personagem': cast_member.get('character'),
                                    'profissao': cast_member.get('known_for_department')
                                })

                    # Obter informações sobre o orçamento, receita e produtoras
                    orcamento = movie_details.get('budget', 0)
                    receita = movie_details.get('revenue', 0)
                    produtoras = [produtora['name'] for produtora in movie_details.get('production_companies', [])]

                    # Extrair as informações detalhadas do filme
                    filme_data = {
                        'id': movie_details.get('imdb_id'),
                        'tituloPrincipal': movie_details.get('title'),
                        'tituloOriginal': movie_details.get('original_title'),
                        'anoLancamento': movie_details.get('release_date'),
                        'tempoMinutos': movie_details.get('runtime'),
                        'genero': [genre['name'] for genre in movie_details.get('genres', [])],
                        'notaMedia': movie_details.get('vote_average'),
                        'numeroVotos': movie_details.get('vote_count'),
                        'sinopse': movie_details.get('overview', ''),
                        'idiomas': [language['name'] for language in movie_details.get('spoken_languages', [])],
                        'elenco': elenco,
                        'orcamento': orcamento,
                        'receita': receita,
                        'produtoras': produtoras
                    }

                    filmes_dados.append(filme_data)
                else:
                    print(f"Erro ao buscar detalhes para o filme '{filme}'")
            else:
                print(f"Filme '{filme}' não encontrado.")
        else:
            print(f"Erro ao buscar dados para '{filme}'.")

    # Salvar os dados dos filmes em um arquivo JSON
    arquivo_json = '/tmp/filmes_dados.json'
    with open(arquivo_json, 'w') as f:
        json.dump(filmes_dados, f, indent=4)

    # Fazer upload do arquivo para o S3
    s3_key = s3_path + 'filmes_dados.json'
    client.upload_file(arquivo_json, bucket_name, s3_key)

    # Retornar resposta de sucesso
    return {
        'statusCode': 200,
        'body': json.dumps('Dados dos filmes enviados para o S3 com sucesso!')
    }
