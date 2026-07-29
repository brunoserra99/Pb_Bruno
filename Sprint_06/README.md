# Sprint_06

Ao final da Sprint_06, me aprimorei mais em python onde também já foi assunto da sprint_03 e sprint_04 e sprint_05 este assunto já foi estudado em outras oportunidades mesmo como iniciante... Hoje posso dizer que obtenho um conhecimento entre iniciante e intermediário.

Esta semana foi apresentado os cursos Aws, onde o primeiro teve como maior parte de suas instruções, realizar orientações sobre a certificações da Aws. Mais um nível de aprimoramento e preparação para obtenção da aprovação no exame Aws certified cloud practitioner.

Iniciamos uma exploração mais pratica sobre o laboratório Aws, 

instrução pratica e bem didático sobre algumas funções e funcionalidades que a Aws, Athena, lambda, demonstrando aplicações mais realistas e as necessidades da vida real, sendo desenvolvida nos laboratórios da aws.

Essa duas semanas assistindo aos vídeos aulas, os exercícios, foi muito bom para participar mais da tecnologia que a Aws oferece.

O curso AWS, mostrou exemplos de atividades utilizadas no dia do profissional de Ti, conseguiu realizar uma introdução em sua utilidade, de maneira pratica e bem esclarecedora dessa funções desenvolvidas, esclarecendo bastante o dia dia do desenvolvedor. Lógico que, de maneira superficial mais deixando bem claro como se desenrola o dia a dia desses profissionais.

Certificado do Curso da sprint_05:

Noções básicas de Analytics na AWS – Parte 1 (Português) | Fundamentals of Analytics on AWS – Part 1 (Portuguese)
* [certificado .pdf](<certificados/Noções básicas de Analytics na AWS – Parte 1 (Português)_AWS Skill Builder Course Completion Certificate.pdf>)

Fundamentos de analytics na AWS – Parte 2 (Português) | Fundamentals of Analytics on AWS – Part 2 (Portuguese)

* [certificado .pdf](<certificados/Fundamentos de analytics na AWS – Parte 2 (Português)_AWS Skill Builder Course Completion Certificate.pdf>)

AWS Skill Builder - Serverless Analytics (Portuguese)

* [certificado .pdf](<certificados/Serverless Analytics (Português)_AWS Course Completion Certificate.pdf>)

AWS Skill Builder - Introduction to Amazon Athena (Portuguese)

* [certificado .pdf](<certificados/Introduction to Amazon Athena (Português)_AWS Course Completion Certificate.pdf>)

AWS Skill Builder - AWS Glue Getting Started (English)

* [certificado .pdf](<certificados/AWS Glue Getting Started_AWS Course Completion Certificate.pdf>)

AWS Skill Builder - Amazon EMR Getting Started (English)

* [certificado .pdf](<certificados/Amazon EMR Getting Started_AWS Skill Builder Course Completion Certificate.pdf>)

Getting Started with Amazon Redshift (Portuguese)

* [certificado .pdf](<certificados/Getting Started with Amazon Redshift (Português)_AWS Course Completion Certificate.pdf>)

AWS Skill Builder - Best Practices for Data Warehousing with Amazon Redshift (Portuguese)

* [certificado .pdf](<certificados/RETIRING - 2025-01-23 Best Practices for Data Warehousing with Amazon Redshift (Portuguese)_AWS Course Completion Certificate.pdf>)

AWS Skill Builder - Amazon QuickSight - Getting Started (English)

* [certificado .pdf](<certificados/Amazon QuickSight - Getting Started_AWS Course Completion Certificate.pdf>)

## Exercícios "utilizando a plataforma Amazon Web Services (AWS)"

Foi solicitado três exercícios, um no aws athena, e outro no aws lambda, afim de melhorar nossa familiaridade com a plataforma e melhorar a experiência com a mesma.

Porem no o primeiro foi sobre criar um bucket no s3, para o armazenamento do conteiner, e outros arquivos que serão necessários para seguir as sprints. como já havia realizado na sprint_05 não foi necessário re fazer este exercício.

No lab athena, foi desenvolvido a configuração do bucket, criação do banco de dados, e criado um tabela apartir da manipulação desse banco de dado, afim de gerar alguns resultados para desenvolvimento do exercício.

Criando o banco de dados:
![evidencia 01](<evidencias/Captura1.png>)

Resultado do item 4 da descrição:
![evidencia 02](<evidencias/Captura2.png>)

Resultado do item 5, da descrição:
![evidencia 03](<evidencias/Captura3.png>)

Os códigos foram fornecidos, e os mesmos foram aplicados no próprio ambiente.

Segue o arquivo de código do item 5. Que foi criado para finalizar o exercício:
* [Script_3x_decada](exercicios/lab_athena/script_3x_decada.txt)

No lab lambda foi estimulado a criação de funções lambda, junto com a ferramenta docker, foi desenvolvido a configuração do ambiente, o desenvolvimento do código, e o teste do código.
A criação da um layer foi solicitada, a partir da função já criada e manipulada com o auxílio do docker para a configuração do ambiente python.

Segue os arquivos necessários, para realizar o exercício:

* [Contêiner docker](exercicios/Docker/minha-camada-pandas.zip)

* [Arquivo docker](exercicios/lab_lambda/Docker/Dockerfile)

* [Script](exercicios/lab_lambda/Docker/script)

## Desafio
Entrego os códigos que foram criados para o desenvolvimento do desafio.

### Etapa 01 

Foi solicitado que criarmos algumas questões para a manipulação de um arquivo de base de dados para usarmos de base para daqui, ate o final do programa de bolsas.
Segue o readme com as questões e um abrisse explicação sobre o porque delas:
* [Questões ](desafio/questoes.md)

### Etapa 02 o desafio.

Solicitado que fosse lido com python dois arquivos .csv, e carregado para o s3 por código para um bucket e um caminho que foi solicitado, junto a criação de um contêiner docker, tudo rodando dentro da minha maquina e atuando junto a aws.
Segue os arquivo criados

* [script](desafio/script.py)

* [Arquivo docker](desafio/dockerfile)

* [movies.csv](desafio/movies.csv)

* [requirements.txt](desafio/requirements.txt)

* [series.csv](desafio/series.csv)

como observação os arquivo, series, e movies, foram alterados apenas para poder subir para o git. logo que devido ao tamanho houve relatos de inconsistências e problemas quando realizado o uploading....
também foi alterado o arquivo .env onde contem as credenciais. que foram mudadas par id_XXXX.
