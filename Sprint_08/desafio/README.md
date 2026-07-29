# Desafio sprint_08


### Objetivo

Familiarização com a linguagem python, biblioteca pandas e boto3, laboratório aws lambda, glue, crawlers para Athena e o serviço AWS no geral, e a manipulação de arquivos no aws s3.
Aprendendo sobre o ambiente Aws e a utilização dos comandos, para upload, download e criação e execução de buckets no ambiente Aws, e funções na lambda e glue, entre outras.

### Descrição

Desenvolver script para realizar para realizar a manipulação dos arquivos da camada RAW, para camada Trusted, transformando os de json e csv, para formato Parquet, e configuração de ambiente aws, para posteriormente a manipulação em base de dados no athenas. Gerando e simulando experiências próximas da realidade, para aprendizado sobre os assuntos. Entregar tudo de maneira organizada no repositório do github.

### Etapas para realização do desafio

* Criar e desenvolver o script em python
* Utilizar bibliotecas solicitadas (, boto3)
* Rodar o script, com comandos, em maquinas locais e no aws do s3.
* Realizar teste e verificar as funcionalidades 
* Finalizar arquivo e estruturas a serem entregues
* Finalizar no repositório do github

### Correção do arquivo json

Como relatado no readme da sprint_08, devido a estudos e um melhor entendimento do que foi solicitado, foi necessário refazer a extração de dados, do Tmdb pois os mesmos não havia capturado os dados necessário.

Segue evidencias do que foi alterado e antes/depois

Evidencia do trecho do código que foi corrigido.
![evidencia 22](<../evidencias/c1.png>)

Evidencia das alterações do arquivo json.
![evidencia 23](<../evidencias/c2.png>)

Segue o script realizado:
* [script(correcao_sprint07).py](../desafio/correcao_desafio_sprint_07/script(correcao_sprint07).py)

O caminho no bucket dos arquivos velhos/errados, permanece no bucket, essa nova extração foi nomeada seguindo a estrutura solicitada, com a data atual. (2025/02/03)

Evidencia do local dos arquivos json.
![evidencia 24](<../evidencias/c3.png>)

*** como não sabia onde colocar esta correção optei por criar uma nova pasta dentro do desafio e colocar o novo código dentro.

**questões alteradas em relação a sprint_06.
* [Questões](../../Sprint_07/desafio/questoes.md)

### Construção do desafio
Iniciei a construção do desafio preparando e desenvolvendo um esboço do programa.
Neste esboço, gerei o arquivo script.py com o que era mais relevante para desenvolver o desafio e a partir desse texto, comecei o desenvolvimento do script.

### Etapa01 

Foi realizado a configuração do ambiente aws Glue, e partir desse ambiente desenvolvo o script para a manipulação dos arquivos csv e json, respectivamente. 

Evidencia config ambiente glue.
![evidencia 25](<../evidencias/d1.png>)

Evidencia execução do script para arquivos csv.
![evidencia 26](<../evidencias/d3.png>)

Evidencia da criação do Crawlers para Athena para arquivos json.
![evidencia 27](<../evidencias/d4.png>)

Evidencia da criação do Crawlers para Athena para arquivos csv.
![evidencia 28](<../evidencias/d5.png>)

segue arquivos usado e os arquivos gerados:

Segue o script realizado:
* [Script_ex02](../desafio/script_json.py)

Segue o script realizado:
* [Script_ex02](../desafio/script_csv.py)

Arquivos prontos para o decorrer da sprint_09, já estão em nuvem e prontos para as manipulações em Sql, e assim prosseguir com a formulação para as respostas das questões.


### Desafio finalizado!!!
