# Sprint_07

Ao final da Sprint_07, me aprimorei mais em python onde também já foi assunto da sprint_03 e sprint_04, sprint_05 e sprint_06, este assunto já foi estudado em outras oportunidades mesmo como iniciante... Hoje posso dizer que obtenho um conhecimento entre iniciante e intermediário.

Esta semana não foi apresentado os cursos Aws, porem inicie os estudos para certificação me aprimorando e preparando para obtenção da aprovação no exame Aws certified cloud practitioner.

Em contra partida foi apresentado exercícios sobre o upload de arquivos obtidos por meio de API, de uma data base de filmes o TMDB, e a manipulação de dados dentro do AWS Cloud s3, e a transformação de dados em formato json, e arquivos com 100 descrições, salvo em caminhos solicitados.

Foi usado também, ferramenta docker, spark, hadoop, entre outras para que o mesmo pudesse ser realizado de maneira satisfatória e condizentes com as instruções fornecidas.

A exploração mais pratica do laboratório Aws, sobre algumas funções e funcionalidades que a Aws, s3, Athena, lambda, Glue, Iam demonstrando aplicações mais realistas e as necessidades da vida real, que são desenvolvidas nos laboratórios da aws, e o dia dia do desenvolvedor.

Essa duas semanas assistindo aos vídeos aulas, os exercícios, foi muito bom para participar mais da tecnologia que a Aws oferece.

O curso AWS, mostrou exemplos de atividades utilizadas no dia do profissional de Ti, conseguiu realizar uma demonstração em sua utilidade, de maneira pratica e bem esclarecedora dessa funções desenvolvidas, esclarecendo bastante o dia dia do desenvolvedor. Lógico que uma pequena experiência porem bem claro como se desenrola o dia a dia desses profissionais.

O apresentado um curso de Spark com Pyspark para o aprendizado prévio do assunto e a possibilidade da realização das atividades. o curso foi desenvolvido em ambiente Linux e desenvolvido por VM-Virtual Machine. O mesmo conseguiu apresentar acredito que o básico e o necessário para o desenvolvimento das atividades.

# Certificado do Curso da sprint_07:

Esta sprint, não teve cursos que geram certificados.

* [Não possui certificado](< >)

## Exercícios

## Exercícios 01

Foi solicitado três exercícios, o primeiro um exercício que trazia familiaridade com o pyspark, e o uso do docker para poder gerar a imagem onde seria rodado o Pyspark. assim dando a possibilidade de gerar um contador de palavras, que foi usado para contar as palavras do readme.md que conta na pagina principal deste repositório. Foi realizado o download deste arquiovo par que fosse realizado a tarefa.

abrindo o Jypiter Notebook, pela imagem docker que foi baixada.
![evidencia 01](<evidencias/Captura de tela 2025-01-19 162314.png>)
comando: (docker run -it -p 8888:8888 jupyter/all-spark-notebook)

jupyter aberto
![evidencia 02](<evidencias/Captura de tela 2025-01-19 162336.png>)

Iniciando o pyspark
![evidencia 03](<evidencias/Captura de tela 2025-01-19 162653.png>)
comando: (pyspark)

script linha por linha para chegar ao numero de palavras.
![evidencia 04](<evidencias/Captura de tela 2025-01-19 164929-1.png>)
esta destacado pela cor azul, o download do arquivo, e o script para a contagem e o resultado = 216 palavras

Segue o script realizado:
* [Script_ex01](exercicios/contador_palavras/script_ex01.txt)

#### exercicio 01 finalizado

## Exercícios 02

Foi realizado que por meio de API, fosse extraído dados do TMDB. Para familiaridade com a plataforma e como realizar o mesmo, 
OBS: as credenciais foram retiradas do código e substituidadas por "API_TMDB_KEY" , mantendo a privacidade conforme solicitado.

Após o cadastro na plataforma, o próximo passo era reescrever o script que foi fornecido, para que fosse gerado dados para o aprendizado.

código executado
![evidencia 05](<evidencias/Captura de tela 2025-01-19 170037.png>)

Segue o script realizado:
* [Script_ex02](exercicios/tmdb/ex.py)

#### exercicio 02 finalizado

## Exercícios 03

Na AWS, foi fornecido um pdf para realizar atividade no AWS Glue. junto com esse pdf foi fornecido um arquivo para que fosse extraído informações do mesmo.

realizado a construção do bucket, e a estrutura de pastas para que fosse carregado o arquivo nomes.csv.
![evidencia 06](<evidencias/Captura de tela 2025-01-19 170829.png>)

realizado o IAM e perfil Awsglueservicerole-lab4
![evidencia 07](<evidencias/Captura de tela 2025-01-19 171625.png>)

realizado o IAM e perfil Awsglueservicerole-lab4
![evidencia 08](<evidencias/Captura de tela 2025-01-19 172142.png>)

realizado conta para utilizar o AWS Glue
![evidencia 09](<evidencias/Captura de tela 2025-01-19 172148.png>)

realizado as permissões no AWS Lake Formation
![evidencia 10](<evidencias/Captura de tela 2025-01-19 172153.png>)

realizado as permissões no AWS Lake Formation
![evidencia 11](<evidencias/Captura de tela 2025-01-19 172158.png>)

realizado o job no AWS Glue/ job details
![evidencia 12](<evidencias/Captura de tela 2025-01-19 172949.png>)

realizado o código de exemplo
![evidencia 13](<evidencias/Captura de tela 2025-01-19 173438.png>)

realizado a execucao do codigo. succeeded
![evidencia 14](<evidencias/Captura de tela 2025-01-19 173516.png>)

realizado alterações no código conforme solicitado.
![evidencia 15](<evidencias/Captura de tela 2025-01-19 173957.png>)

resultado do código criado
![evidencia 16](<evidencias/Captura de tela 2025-01-19 174445.png>)

criando crawler
![evidencia 17](<evidencias/Captura de tela 2025-01-19 184005.png>)

criando crawler
![evidencia 18](<evidencias/Captura de tela 2025-01-19 184029.png>)

criando crawler/finalizado
![evidencia 19](<evidencias/Captura de tela 2025-01-19 184333.png>)

Glue finalizado
![evidencia 20](<evidencias/Captura de tela 2025-01-19 184509.png>)

Glue finalizado/resultado
![evidencia 21](<evidencias/Captura de tela 2025-01-19 184557.png>)

script usado para gerar os resultados
[script](exercicios/glue/script.py)

csv fornecido para gerar os resultados
[script](exercicios/glue/nomes.csv)

#### exercicio 03 finalizado

## Desafio
Entrego os códigos que foram criados para o desenvolvimento do desafio.


Foi solicitado a criacao de uma camada para a ingestão de libs, logo após foi introduzido o código que foi desenvolvido durante a sprint_07.
E executado localmente, até a finalização do mesmo e assim realizado sua execução em lab AWS...
Foi encontrados erros e corrigido até obter sucesso.

E assim a importação dos dados via APIs, e a transformação desses dados em arquivos json de no Maximo itens por arquivo, de no Maximo 10mb foi concluída tendo seu resultado, no próprio repositório da AWS. e portanto finalizando o desafio com sucesso.

segue arquivos usado e os arquivos gerados:

* [script](desafio/script.py)

criando a função
![evidencia 22](<evidencias/Captura de tela 2025-01-19 233312.png>)

criando a camada
![evidencia 23](<evidencias/Captura de tela 2025-01-19 233534.png>)

resultado gerado
![evidencia 24](<evidencias/Captura de tela 2025-01-20 000045.png>)

resultado no s3
![evidencia 25](<evidencias/Captura de tela 2025-01-20 003914.png>)

*** Também foi alterado o arquivo, onde contem as credenciais. que foram mudadas par id_XXXX.

###
Altero as questões que foram sugeridas na sprint_07, segue o novo arquivo:

* [Questoes](desafio/questoes.md)
