# Desafio sprint_07

### Objetivo

Familiarização com a linguagem python, biblioteca pandas e boto3, laboratório aws lambda, glue, e o servico AWS no geral, e a manipulação de arquivos no aws s3.
Aprendendo sobre o ambiente Aws e a utilização dos comandos, para upload, download e criação e execução de buckets no ambiente Aws, e funcoes na lambda e glue, entre outras.

### Descrição

Desenvolver script para realizar o upload de arquivos, via APis, do TMDB para manipulacao na AWS. Para simular e gerar experiências próximas da realidade, para aprendizado sobre os assuntos. Entregar tudo de maneira organizada no repositório do github.

### Etapas para realização do desafio

* Assistir as trilhas sobre o conteúdo
* Baixar arquivos necessários
* Criar e desenvolver o script em python
* Utilizar bibliotecas solicitadas (, boto3)
* Rodar o script, com comandos, em maquinas locais e no aws do s3.
* Realizar teste e verificar as funcionalidades 
* Finalizar arquivo e estruturas a serem entregues
* Finalizar no repositório do github

### Evolução das Questões

**questoes alteradas em relacao a sprint_06.
* [Questões](../desafio/questoes.md)

### Construção do desafio
Iniciei a construção do desafio preparando e desenvolvendo um esboço do programa.
Neste esboço, gerei o arquivo script.py com o que era mais relevante para desenvolver o desafio e a partir desse texto, comecei o desenvolvimento do script.

### Etapa01 

Foi criado o arquivo script.py onde contem os códigos responsáveis pela busca e realizacao do upload de arquivos, para o aws s3, por meio de api, e onde os dados sao salvos em arquivos em .json, mantendo o maximo de 100 itens por arquivos, e salvos em estruturas comforme solicitados.

Junto ao desenvolvimento, foi realizado teste localmentes para a definiçao do codigo. e pequenas modificaçoes dentro da Aws.

***Lembrando que, o arquivo foi altera para que as credencias fosse mantido em segurança, no local da mesma foi adicionado: id_xxx

Os arquivos que foram usados para desenvolver o desafio 

* [script](script.py)

Todos os comandos estao dentro do arquivo, e a sequencia seguiu os passo que foram descritos nos cursos realizado no decorrer do programa, e exercicio aplicados.



----------------------------------------------------------------------------

### Etapa02 - Script rodando

Segue as evidencias do script rodando:

criando a função
![evidencia 22](<../evidencias/Captura de tela 2025-01-19 233312.png>)

criando a camada
![evidencia 23](<../evidencias/Captura de tela 2025-01-19 233534.png>)

resultado gerado
![evidencia 24](<../evidencias/Captura de tela 2025-01-20 000045.png>)

resultado no s3
![evidencia 25](<../evidencias/Captura de tela 2025-01-20 003914.png>)




###Desafio finalizado!!!
