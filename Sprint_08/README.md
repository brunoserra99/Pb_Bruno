# Sprint_08
Ao final da Sprint_08, me aprimorei mais em python onde também já que foi assunto da sprint_03 e sprint_04, sprint_05, sprint_06 e sprint_07, este assunto já foi estudado em outras oportunidades mesmo como iniciante... Hoje posso dizer que obtenho um conhecimento entre iniciante e intermediário.

Esta semana não foi apresentado os cursos Aws, porem os estudos para certificação me aprimorando e preparando para obtenção da aprovação no exame Aws certified cloud practitioner.

Nesta sprint realizamos exercícios para geração de massa de dados, de maneira aleatório e como podemos utilizar os mesmo para criar os datasets.

Em contra partida foi apresentado exercícios sobre para manipulação de arquivos usando pyspark, e como comandos spark SQL, como adicionar colunas, e atribuir valores aleatórios e também aleatórios em um contexto pré estipulado, registro de tabela, temporária para executar os comandos SQL, filtros SQL, e ordenando filtros crescentes, por colunas, 

Foi solicitado também o exercício de extração de dados utilizando a APi do TMDB, onde sobe orientação de que se já tivesse sido realizado na sprint anterior, era apenas para repetir os arquivos sem necessidade de execução.

Foi realizado o upload de arquivos obtidos por meio de API, de uma data base de filmes o TMDB, e a manipulação de dados dentro do AWS Cloud s3, e a transformação de dados em formato json, e arquivos com 100 descrições, salvo em caminhos solicitados.

A exploração mais pratica do laboratório Aws, sobre algumas funções e funcionalidades que a Aws, s3, Athena, lambda, Glue e Iam demonstram aplicações mais realistas e as necessidades da vida real, que são desenvolvidas nos laboratórios da aws, e o dia dia do desenvolvedor.

E a manipulação de dados dentro da Aws movendo os arquivos para a camada Truster, coloca em pratica bem a vivencia e funcionalidades do dia dia do analista de dados.

Essa duas semanas assistindo aos vídeos aulas, os exercícios, foi muito bom para participar mais da tecnologia que a Aws oferece.

O curso AWS, mostrou exemplos de atividades utilizadas no dia do profissional de Ti, conseguiu realizar uma demonstração em sua utilidade, de maneira pratica e bem esclarecedora dessa funções desenvolvidas, esclarecendo bastante o dia dia do desenvolvedor. Lógico que uma pequena experiência porem bem claro como se desenrola o dia a dia desses profissionais.

O desenvolvimento dos scripts foram realizados, por meio de notebooks no colab, onde foi utilizado recursos com pyspark, python, e Sql. E atividades dentro Aws S3.

montando o driver e instalando spark/hadoop/pyspark
![evidencia 01](<evidencias/1.png>)

Configurando as variáveis de ambientes
![evidencia 02](<evidencias/2.png>)

iniciando sessão
![evidencia 03](<evidencias/3.png>)

# Certificado do Curso da sprint_08:

Esta sprint, não teve cursos que geram certificados.

* [Não possui certificado](< >)

# Exercícios

## Exercícios 01

### 3.1
O Primeiro exercício, foi solicitado para inicializar um lista contendo 250 números inteiros, de forma aleatória.

código executado
![evidencia 04](<evidencias/4.png>)

Segue o arquivo salvo:
* [lista.csv](exercicios/ex_01_e_02/lista.csv)

### 3.2
Iniciar uma lista contendo 20 números de animais, em ordem crescente, e salvar em arquivo .csv.

código executado
![evidencia 05](<evidencias/5.png>)

Segue o arquivo salvo:
* [animais.csv](exercicios/ex_01_e_02/animais.csv)

### 3.3
E finalizando, importar uma biblioteca especifica, random, times, names. Para geração do dataset nomes aleatórios e quantidade de nomes únicos, gerar os nomes aleatoriamente e criar um arquivo nomes_aleatorios.txt, como nomes um em cada linha.

Especificação:
![evidencia 06](<evidencias/6.png>)

código executado
![evidencia 07](<evidencias/7_resultado.png>)

Segue o arquivo salvo:
* [nomes_aleatorios.txt](exercicios/ex_01_e_02/nomes_aleatorios.txt)

#### exercício 01 finalizado


## Exercícios 02

Foi utilizado o arquivo nome_aleatorios.txt do exercício anterior, para o decorrer do exercício.


### 3.1
Na preparação do ambiente, baixado as bibliotecas necessária e definido a spark Session, para podes usar o spark Sql.

Iniciamos o script, com a leitura do arquiavo nome_aleatorios.txt, e carregamos ele para o dataframe.

código executado a preparação do ambiente e a inicialização do arquivo nome_aleatorios.txt

![evidencia 8](<evidencias/8.png>)

Segue o arquivo:
* [nomes_aleatorios.txt](exercicios/ex_01_e_02/nomes_aleatorios.txt)

*** devido o arquivo ser maior de 100mb foi retirado alguns nomes para poder upar o mesmo para o repositório assim ficando fácil a visualização


### 3.2
Apresentação do schema, com todas as colunas como string, e foi renomeado a coluna para nomes.

código executado
![evidencia 9](<evidencias/9.png>)


### 3.3
Adicionado a coluna escolaridade, e atribuído de forma aleatória fundamental, médio e superior. 

código executado
![evidencia 10](<evidencias/10.png>)


### 3.4
Adicionado a coluna pais, e atribuído um nomes dos 13 países da America do sul de forma aleatória.

código executado
![evidencia 11](<evidencias/11.png>)


### 3.5
Adicionada uma coluna AnoNascimento e atribuído aleatoriamente um ano entre 1945 e 2010 

código executado
![evidencia 12](<evidencias/12.png>)


### 3.6
Selecionadas as pessoas que nasceram neste século, armazenado em outro dataframe e apresentado as 10 primeiras linhas

código executado
![evidencia 13](<evidencias/13.png>)


### 3.7
Foi realizado o mesmo processo anterior, porem utilizando o sparkSQL

código executado
![evidencia 14](<evidencias/14.png>)


### 3.8
Usando o método filter foi contado o numero de pessoas que são da geração mellennials, (1980 a 1994).

código executado
![evidencia 15](<evidencias/15.png>)


### 3.9
Foi repetido o processo acima em sparkSql

código executado
![evidencia 16](<evidencias/16.png>)


### 3.10
Utilizando o sparkSql, foi obtido a quantidade de pessoas de cada pais par cada geração (baby boomers, geração x, millennials, geração z), armazenado em um novo dataframe, e apresentados em ordem crescente, por pais, geração e quantidade.

código executado
![evidencia 17](<evidencias/17.png>)

#### exercício 02 finalizado


## Exercícios 03

Foi realizado que por meio de API, fosse extraído dados do TMDB. Para familiaridade com a plataforma e como realizar o mesmo, 
OBS: as credenciais foram retiradas do código e substituídas por "API_TMDB_KEY" , mantendo a privacidade conforme solicitado.

Após o cadastro na plataforma, o próximo passo era reescrever o script que foi fornecido, para que fosse gerado dados para o aprendizado.

código executado
![evidencia 21](<evidencias/Captura de tela 2025-01-19 170037.png>)

Segue o script realizado:
* [Script_ex02](exercicios/tmdb/ex.py)

#### exercício 03 finalizado


## Realizado correção no script do desafio da sprint_07

*** Após estudar e verificar o desenvolvimento futuro do desafio, percebi algumas colunas minhas não continha dados e desta maneira fui obrigado a realizar uma nova extração de dado junto a API do TMDb, para que pudesse buscar os dados da coluna, receita, orçamento, e produtora.

Evidencia do trecho do código que foi corrigido.
![evidencia 22](<evidencias/c1.png>)

Evidencia das alterações do arquivo json.
![evidencia 23](<evidencias/c2.png>)

Segue o script realizado:
* [script(correcao_sprint07).py](desafio/correcao_desafio_sprint_07/script(correcao_sprint07).py)

O caminho no bucket dos arquivos velhos/errados, permanece no bucket, essa nova extração foi nomeada seguindo a estrutura solicitada, com a data atual. (2025/02/03)

Evidencia do local dos arquivos json.
![evidencia 24](<evidencias/c3.png>)

*** como não sabia onde colocar esta correção optei por criar uma nova pasta dentro do desafio e colocar o novo código dentro.

##### correção finalizada


## Desafio

Desafio
Entrego os códigos que foram criados para o desenvolvimento do desafio.

Inicio o desafio realizando a configuração do ambiente aws Glue, e partir desse ambiente desenvolvo o script para a manipulação dos arquivos csv e json, respectivamente. 

Evidencia config ambiente glue.
![evidencia 25](<evidencias/d1.png>)

Evidencia execução do script para arquivos csv.
![evidencia 26](<evidencias/d3.png>)

Evidencia da criação do Crawlers para Athena para arquivos json.
![evidencia 27](<evidencias/d4.png>)

Evidencia da criação do Crawlers para Athena para arquivos csv.
![evidencia 28](<evidencias/d5.png>)

segue arquivos usado e os arquivos gerados:

Segue o script realizado:
* [Script_ex02](desafio/script_json.py)

Segue o script realizado:
* [Script_ex02](desafio/script_csv.py)


#### Desafio finalizado

*** Também foi alterado o arquivo, onde contem as credenciais. que foram mudadas par id_XXXX.

###
Arquivo das questões:

* [Questões](../Sprint_07/desafio/questoes.md)
