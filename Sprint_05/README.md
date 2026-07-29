# Sprint_05

Ao final da Sprint_05, me aprimorei mais em python onde também já foi assunto da sprint_03 e sprint_04, este assunto já foi estudado em outras oportunidades mesmo como iniciante... Hoje posso dizer que obtenho um conhecimento entre iniciante e intermediário.

Esta semana foi apresentado os cursos Aws, onde o primeiro teve como maior parte de suas instruções, realizar orientações sobre a certificações da Aws. Mais uma nível de aprimoramento e preparação para obtenção da aprovação no exame Aws certified cloud practitioner.... O curso também foca em entender melhor o modelo de responsabilidades, praticas recomendadas, e aspectos econômicos.

Iniciamos uma exploração mais pratica sobre o laboratório Aws, foi fornecido o jogo com instruções praticas e bem didático sobre algumas funções e funcionalidades que a Aws permite realizar com algumas necessidades da vida real, sendo desenvolvida em uma cidade que vem se aprimorando para o turismo, e o suprimento de suas demandas.

Essa duas semanas assistindo aos vídeos aulas, e realizando o game do cloud partitioner foi muito bom para participar mais da tecnologia que a Aws oferece.

O curso AWS, mostrou exemplos de atividades utilizadas no dia do profissional de Ti, conseguiu realizar uma introdução em sua utilidade, de maneira pratica e bem esclarecedora dessa funções desenvolvidas, esclarecendo bastante o dia dia do desenvolvedor. Lógico que, de maneira superficial mais deixando bem claro como se desenrola o dia a dia desses profissionais.

Certificado do Curso da sprint_05:

## Curso-padrão de preparação para o exame: AWS Certified Cloud Practitioner (CLF-C02 - Português (Brasil))

* [certificado .pdf](<certificados/18719_5_6576231_1734409204_AWS Skill Builder Course Completion Certificate.pdf>)

#### Este curso gerou um acesso a outro curso da AWS: AWS Cloud Practitioner Essentials
* [certificado .pdf](<certificados/134_3_6576231_1734953751_AWS Course Completion Certificate.pdf>)

## O link disponibilizado ao final do jogo: AWS Skill Builder - AWS Cloud Quest: Cloud Practitioner

* [arquivo no repositorio](<certificados/Certificado_cloud_quest.txt>)

* [Link conclusão do jogo](Removido devido a dados sensíveis)

## Exercícios "utilizando a plataforma Amazon Web Services (AWS)"

Como meio de testar o nosso acesso foi solicitado, alguns passo para confirma o acesso e familiaridade ao Amazon Web Services - Aws.

Segue alguma imagens sobre o passo a passo realizado. Logo que o mesmo solicita que após a verificação das credenciais, seja realizada a criação de um instância EC2, e a mesma rode por alguns minutos e que fosse excluída.

Criando a instancia

![evidencia 01](<evidencias/1Captura.png>)

Executando a instancia

![evidencia 02](<evidencias/2Captura.png>)

Finalizando a instancia

![evidencia 03](<evidencias/3Captura.png>)

Instancia encerrada

![evidencia 05](<evidencias/5Captura.png>)


## Exercício Criando bucket

Foi dado instruções para que fosse gerado um bucket,

![evidencia 05](<evidencias/Captura5.png>)

segue o link:

* [bucket Aws](http://bucketbsaws.s3-website-us-east-1.amazonaws.com/)

Segue a evidencia dos arquivos index.html, erro.html e a pasta dado/nomes.zip

![evidencia 06](<evidencias/Captura6.png>)

O site no ar:

![evidencia 07](<evidencias/Captura7.png>)


## Desafio
Entrego os códigos que foram criados para o desenvolvimento do desafio.

### Etapa 01 - Busca da base de dados

A busca da base de dados foi realizada no site dados.gov.br, e a base que mais se enquadrou ao meu ver para realização do desafio foi o sistema de transporte de servidores públicos taxigov v2
dentro dessa base de dados existe alguns recursos e um dele foi o recurso dos últimos 7 dias 
segue o link:
* [base de dados](https://dados.gov.br/dados/conjuntos-dados/sistema-de-transportes-de-servidores-publicos---taxigov-v2)

e o link do arquivo para download e:

* [Download base de dados](https://repositorio.dados.gov.br/seges/taxigov/v2/taxigov-corridas-7-dias.zip)

### Etapa 02 - Script upload

Foi solicitado a criação de um arquivo para iniciar um bucket, e realizar o upload do arquivo original, e junto com esse script, as credencias da Aws, para que o acesso e a inicialização do bucket ocorressem tudo bem, sendo utilizado a biblioteca boto3.

segue o script de upload:

* [Script upload](desafio/script_up.py)

Foi solicitado 6 manipulações diversas, onde as mesmos estão listadas, assim como uma pergunta/questão envolvendo todas elas, que esta neste readme em Markdown:

* [Questão](desafio/questao.md)

### Etapa 03 - Manipulação, resultado e upload do arquivo modificado

Foi desenvolvido um script, onde ocorreu a manipulação da base de dados, e onde foram resolvidos os itens cobrados, logo após a resolução dos questionamentos, foi gerado um resultados, para gerar os resultados foi utilizados biblioteca pandas, assim foi realizado o upload dos arquivos para o servidos s3 Aws, utilizando a biblioteca boto3. Segue o script:

* [Script Manipulação](desafio/script_manipulacao.py)

obs: As manipulações seguiram as questões contidas no:

* [Questão](desafio/questao.md)
