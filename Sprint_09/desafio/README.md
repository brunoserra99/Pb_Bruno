# Desafio sprint_09

### Objetivo

Familiarização com a linguagem python, biblioteca pandas e boto3, laboratório aws lambda, glue, Crawlers, Athena e o serviço AWS no geral, e a manipulação de arquivos no aws s3.
Aprendendo sobre o ambiente Aws e a utilização dos comandos, para upload, download e criação e execução de buckets no ambiente Aws, e funções na lambda e glue, comandos Sql e entre outras.

### Descrição

Desenvolver script para realizar a manipulação dos arquivos da camada trusted, para camada Refined, transformando e modelando os arquivos Parquet para analises posteriores, e configuração de ambiente aws, para posteriormente realizar a  manipulação e as analises para insights na base de dados. Gerando e simulando experiências próximas da realidade, para aprendizado sobre os assuntos. Entregar tudo de maneira organizada no repositório do github.

### Etapas para realização do desafio

* Criar modelagem dos dados
* Manipulação dos dados entre camadas do data laker
* Criar e desenvolver o script em python
* Utilizar bibliotecas solicitadas (, boto3)
* Rodar o script, com comandos, em maquinas locais e no aws do s3.
* Realizar teste e verificar as funcionalidades 
* Finalizar arquivo e estruturas a serem entregues
* Finalizar no repositório do github


### Construção do desafio
Inicio o desafio realizando, desenvolvendo o modelo dimensional:

Evidencia config ambiente glue.
![diagrama](<../evidencias/diagrama_final.png>)

Após a criação do diagrama, sigo coma  configuração da estrutura de pastas, para a  camada Refined, e posteriormente o ambiente Aws Glue, e partir desse ambiente desenvolvo o script para a manipulação dos arquivos da camada Trusted para a Refined, onde gero os dados da tabela Fato_ , e Dimensao_. 

Evidencia config ambiente glue.
![evidencia 01](<../evidencias/01.png>)

Evidencia execução do script.
![evidencia 02 - parte 1](<../evidencias/2.png>)

Evidencia execução do script.
![evidencia 02 - parte 2](<../evidencias/02.png>)

Evidencia da estruturação das pasta.
![evidencia 03](<../evidencias/03.png>)

Evidencia da estruturação das pasta.
![evidencia 04](<../evidencias/04.png>)

Evidencia da estruturação das pasta.
![evidencia 05](<../evidencias/05.png>)

Evidencia da estruturação das pasta.
![evidencia 06](<../evidencias/06.png>)

Segue o script realizado:
* [Script_desafio](../desafio/script.py)


Evidencia da criação do Crawlers.
![evidencia 07](<../evidencias/07.png>)

Evidencia da criação do Crawlers.
![evidencia 08](<../evidencias/08.png>)

Evidencia para comandos Sql no Athena.

Evidencia do comando Sql Athena (dim_artista).
![evidencia 09](<../evidencias/09.png>)

Evidencia do comando Sql Athena (dim_filme).
![evidencia 10](<../evidencias/10.png>)

Segue trechos do código:

Trecho do script, gera a estrutura de pasta (destino)
![evidencia 11](<../evidencias/11.png>)

Trecho do script, leitura dos arquivos na camada Trusted, e realiza a união das colunas em um dataframe.
![evidencia 12](<../evidencias/12.png>)

Trecho do script, geração da tabela FATO.
![evidencia 13](<../evidencias/13.png>)

Trecho do script, gerando as tabela dim_... .
![evidencia 14](<../evidencias/14.png>)

Trecho do script, salvando os arquivos conforme a modelagem.
![evidencia 15](<../evidencias/15.png>)

### Desafio finalizado!!!



