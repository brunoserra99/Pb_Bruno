# Desafio sprint_04


### Objetivo

Familiarização com a linguagem python, e a ferramenta docker, aprendendo sobre instalação de programas e a utilização dos comandos, para criação e execução de imagens e conteiner para facilitar tarefas e melhorar aplicações.

### Descrição

Desenvolver funções de uso cotidiano na Linguagem Python, e o desenvolvimento de scripts que rodem dentro de containers do docker, contendo interação com o usuário. E entregar tudo de maneira organizada no repositório do github.

### Etapas para realização do desafio

* Assistir as trilhas sobre o conteúdo
* Baixar arquivos necessários
* Criar e desenvolver o script em python
* Criar imagem e conteiners no docker
* Rodar o script, com comandos pelo terminal/docker
* Realizar teste e verificar as funcionalidades 
* Finalizar arquivo e estruturas a serem entregues
* Finalizar no repositório do github

### Construção do desafio
Iniciei a construção do desafio preparando e desenvolvendo um esboço do programa.
Neste esboço, gerei um bloco de notas com o que era mais relevante sobre a apresentação dos slides do desafio, facilitando o entender e a manipulação dos mesmos.

### Etapa01
Após a construção do esboço, dei inicio a etapa01:
Criação do projeto carguru, com a pasta carguru, e o download do arquivo disponibilizado, e também foi criado o arquivo dockerfile:
* [Pasta projeto carguru](carguru)
* [carguru.py](carguru/carguru.py)
* [dockerfile](carguru/Dockerfile)

Ambiente criado:
![Evidencia 01](../evidencias/Captura1.png)

No terminal, foram utilizados alguns comandos para verificar como estava o ambiente, e a necessidade de download de algum arquivo:
Comandos:
docker ps –a 
docker ps  
docker images 

Após a verificação do ambiente, onde a mesma não continha nenhuma imagem:
![Evidencia 02](../evidencias/Captura2.png)

Foi baixado o arquivo python pelo terminal vscode
![Evidencia 03](../evidencias/Captura3.png)
Python baixado e checado c o comando docker images
![Evidencia 04](<../evidencias/Captura3 1.png>)

Como o arquivo carguru.py já estava pronto
Foi desenvolvido as instruções no arquivo dockerfile para que imagem rode. 
![Evidencia 05](../evidencias/Captura4.png)

Criando a imagem carguru_img com o comando:
* docker build -t carguru_img .

E confirmando a criação da imagem carguru_img com o comando:
* docker images

![Evidencia 06](<../evidencias/Captura4 1.png>)

No terminal foi iniciado o contêiner, pelo comando 
* docker run carguru_img

Devido a erro de digitação (docker), a mensagem de erro apareceu...
Novamente: docker run carguru_img, gerou a resposta que vou dirigir um ix-35

![Evidencia 07](../evidencias/Captura5.png)

Executando alguns teste e o resultado:
![Evidencia 08](../evidencias/Captura6.png)
![Evidencia 09](../evidencias/Captura7.png)
![Evidencia 10](../evidencias/Captura8.png)

Contêiner rodando ou encerrado e a imagens utilizadas (carguru_img e python):
Comandos utilizados:
* docker ps –a
* docker ps   
* docker images

![evidencia 11](../evidencias/Captura9.png)

Etapa 01 finalizada!!!
----------------------------------------------------------------------------

### Etapa02

Foi entregue uma pergunta sobre a reutilização do conteiners no docker, se tem como ou não. E solicitado que fosse criado um arquivo markdown segue o arquivo:
[Reposta etapa02](etapa02.md)
![Evidedncia 12](../evidencias/Captura10.png)

Etapa 02 finalizada!!!
----------------------------------------------------------------------------
### Etapa03

Inicio a etapa 03 criando o projeto script_input os arquivos necessário, criado o script do python e o arquivo dockerfile, para execução da etapa03.

![Evidencia 13](../evidencias/Captura11.png)

Desenvolvido o código do script python em sha-1, gerando a hash em hexdigest
![Evidencia 14](../evidencias/Captura12.png)

Foi desenvolvido as instruções no arquivo dockerfile para que imagem rode. 
![Evidencia 15](<../evidencias/Captura12 1.png>)

Criando a imagem do script mascarar-dados  com o comando:
* docker build -t mascarar-dados .
Confirmando a criação da imagem com o comando:
* docker images

![Evidencia 16](../evidencias/Captura13.png)

Inicializando o contêiner a partir da img mascarar-dados, pelo o terminal com o comando:
* docker run -i mascarar-dados
![Evidencia 17](../evidencias/Captura14.png)

Mascaramento realizado com sucesso
![Evidencia 18](<../evidencias/Captura14 1.png>)

Realizando o mascaramento das palavras aleatórias
Palavra: Cloud Computing
![Evidencia 19](../evidencias/Captura15.png)

Palavra: DevOps
![Evidencia 20](../evidencias/Captura16.png)

Palavra: Aws
![Evidencia 21](../evidencias/Captura18.png)

Palavra: Aws
![Evidencia 22](../evidencias/Captura19.png)

#### Obs.:
Mudando a escrita de letras maiúsculas para minúsculas, ocorre a criptografada de maneira diferente. Porem sempre da mesma forma utilizando a mesma palavra, desde que seja mentido a tipo de caixa alta/baixa
![Evidencia 23](../evidencias/Captura19.png)

Conforme solicitado no item 4 da etapa03, o registro:
E segue o script python
[script Python](script_input/mascarar-dados.py)
![Evidencia 24](../evidencias/Captura12.png)


Arquivo docker
[dockerfile](script_input/Dockerfile)
![Evidencia 25](<../evidencias/Captura12 1.png>)


E os comandos utilizados para inicio do contêiner.
![Evidencia 26](../evidencias/Captura14.png)
comando:
* docker run -i mascarar-dados

Etapa 03 finalizada

