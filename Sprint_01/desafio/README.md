# Sprint_01 - Desafio Script Linux e Repositório Github/Markdown

## Script Linux

### Objetivo
Se familiarizar com o Linux: aprender sobre instalação de programas entre eles a Maquina Virtual - VM, e utilizar comando básico do Sistema Operacional - SO e rodar scripts comuns no SO, assim realizando tarefas automizadas e agendadas.

### Descrição

Desenvolver um script que automatize o processo diário para realização de tarefas/backup, em horários específicos, e que a partir de um arquivo base realize a extração de conteúdo específico, unindo e gerando novos arquivos como a data atua como complemento de seu nome.
E por fim criar um script, que quando executado consolide arquivos determinados em apenas em um arquivo, facilitando a visualização.

### Etapas para realização do desafio
* Assistir as trilhas sobre o conteúdo
* Baixar arquivos necessários
* Criar e desenvolver o programa
* Realizar teste e verificar as funcionalidades 
* Realizar agendamento da tarefa
* Verificar a execução.

### Construção do desafio

Visualizar o desafio, e lanço tópicos no arquivo .sh para facilitar a construção do programa.
    * [Criação dos tópicos](/Sprint_01/evidencia/1_etapas.png).
    

Baixo os arquivos necessários, do curso da Udemy. E cria as pastas necessárias.
Desenvolvo a primeira etapa do código com anotações feitas do curso do Linux da trilha.
    * [Print do inicio do programa, e a criação das pastas](/Sprint_01/evidencia/Screenshot1.png).

A tarefa de extração dos dados do arquivo base teve alguma dificuldade e busquei outros conteúdos para realizadas. Em busca do conteúdo realizei muita busca e acabei optando por seguir a linha de raciocínio usando awk.
    * [Desenvolvimento de extração dos dados ](/Sprint_01/evidencia/Screenshot2.png).

Na função do contador de item, que excluem os itens repetidos, tive grande dificuldade, para conseguir realizar muito pouco conteúdo sobre remoção de duplicatas muito conteúdo ruins na internet em sim, sobre a documentação, conseguir alguma informação em alguns fóruns e acabou dando certo. Não sei bem como foi.
* [Função que elimina os itens repetidos do código](/Sprint_01/evidencia/Screenshot3.png).

E a remoção dos arquivos temporários, consegui realizar com o conteúdo da trilha.
* [remoção de arquivos temporários](/Sprint_01/evidencia/Screenshot4.png).

E assim finalizando o primeiro .sh.

No terminal com grande ajuda do meu Squad3 consegui fazer o crontab rodar nas horas agendadas e também em dois em 2 minutos onde rodei grande parte do teste
* [Código para gerenciar o agendamento pelo crontab](/Sprint_01/evidencia/Screenshot5.png).

O desenvolvimento do arquivo consolidados foi tranquilo consegui usar as informação do curdo da trilha finalizei o mesmo mais fácil.
* [Remoção de arquivos temporários](/Sprint_01/evidencia/Screenshot6.png).

Consegui realizar o desenvolvimento do arquivo e estava pronto para começar a roda no dia 23/10 ao rodar o código pelo terminal, rodou tudo normal aparentemente. Porem ao abrir o arquivo relatorio-yyyymmdd.csv o dado da ultima venda estava em branco.
* [Falha no arquivo gerado ](/Sprint_01/evidencia/Screenshot7.png).

Acabou que perdi o tempo para o código funcionar no dia 23/10, junto c a squad3 no final do dia revisamos os código e estava tudo ok novamente. Não foi feito nenhuma alteração no código. Porem estava funcionando novamente. Estava pronto para dar inicio a uma nova execução do código mais uma vez... e novamente tive problema com a data da ultima venda o mesmo problema.
[Nova falha no arquivo gerado ](/Sprint_01/evidencia/Screenshot8.png).

Pesquisando e conversando com pessoas mais experientes minha duvida se consolidou e estava rodando com a ultima linha em branco, logo os dados não existia e a extração do dado e um print em branco.
[Arquivo com o dado data da ultima venda em branco](/Sprint_01/evidencia/Screenshot9.png).

Como solução, manualmente apagar a ultima linha do arquivo base, quando esta não conter dados.

Procuro uma solução para tal problema, ate consegui desenvolver uma porem estou rodando o a ultima vez no dia 28/08/24. Onde esta rodando sem problemas e todos os arquivos têm sido gerados normalmente.
[Arquivo com os dados sendo gerado corretamente.](/Sprint_01/evidencia/Screenshot10.png).

Hoje dia 28/10 o código rodou super bem, e sem intecorrencias.
[Primeira parte do desafio OK.](/Sprint_01/evidencia/Screenshot11.png).

Após finalizar a primeira parte. Logo em seguida manualmente pelo terminal rodo o segundo arquivo .sh. o mesmo roda sem problemas e gera o arquivo [relatatorio-final.txt](/Sprint_01/desafio/ecommerce/vendas/backup/relatorio_final.txt)
[relatório-final.txt](/Sprint_01/evidencia/Screenshot12.png).

### OBS:
Foi confeccionado, arquivos de dados fake, para rodar nos dias listados, esse arquivos possuia dados com data do dia anterio e do dia atual, dando a entender que as vendas acontecia pos 15h27 do dia anterior, athe as 15h27 do dia atual. dados_de_vendas as trocas acontecia com a mudanca manual do final do arquivo apaga o *dados_de_vendas_x.csv* para *dados_de_vendas.csv* 

### Aquivo dia 25/10
[dados_de_vendas_5.csv](/Sprint_01/desafio/ecommerce/dados_de_vendas_5.csv)

### Arquivo dia 26/10
[dados_de_vendas_6.csv](/Sprint_01/desafio/ecommerce/dados_de_vendas_6.csv)

### Arquivo dia 27/10
[dados_de_vendas_7.csv](/Sprint_01/desafio/ecommerce/dados_de_vendas_7.csv)

### Arquivo dia 28/10
[dados_de_vendas.csv](/Sprint_01/desafio/ecommerce/dados_de_vendas.csv)


## Desafio concluído
Segue os Print do conteúdo das pastas
[Conteúdo pasta ecommerce.](/Sprint_01/evidencia/Screenshot13.png).
[Conteúdo pasta ecommerce/vendas](/Sprint_01/evidencia/Screenshot14.png).
[Conteúdo pasta ecommerce/vendas/backup](/Sprint_01/evidencia/Screenshot15.png).
[Conteúdo pasta ecommerce/vendas/backup/relatorio-20241025](/Sprint_01/evidencia/Screenshot16.png).
[Conteúdo pasta ecommerce/vendas/backup/relatorio-20241026](/Sprint_01/evidencia/Screenshot17.png).
[Conteúdo pasta ecommerce/vendas/backup/relatorio-20241027](/Sprint_01/evidencia/Screenshot18.png).
[Conteúdo pasta ecommerce/vendas/backup/relatorio-20241028](/Sprint_01/evidencia/Screenshot19.png).
[Conteúdo pasta ecommerce/vendas/backup/relatorio-final20241028](/Sprint_01/evidencia/Screenshot20.png).

## Documentos Gerados
### Primeiro dia 25/10
[relatatorio-final.txt](/Sprint_01/desafio/ecommerce/vendas/backup/relatorio-20241025.txt)

### Segundo dia 26/10
[relatorio-20241025.txt](/Sprint_01/desafio/ecommerce/vendas/backup/relatorio-20241026.txt)

### Terceiro dia 27/10
[relatorio-20241026.txt](/Sprint_01/desafio/ecommerce/vendas/backup/relatorio-20241027.txt)

### Quarto dia 28/10
[relatorio-20241027](/Sprint_01/desafio/ecommerce/vendas/backup/relatorio-20241028.txt)

### Relatorio gerado ao final dos quatro dias.
[relatorio-20241028.txt](/Sprint_01/desafio/ecommerce/vendas/backup/relatorio_final.txt)



## Repositório Github/Markdown


### Objetivo
Se familiarizar com o GitHub, aprendendo sobre repositório, upload e download de atualizações, e aprender os comandos mais utilizados, aprender sobre instalação dos programas, entre eles a VsCode, e o GIT.

### Descrição
Baixar e instalar programas para a utilização do ambiente de trabalho, criação de repositório e baixar e enviar arquivos e atualização destes, se ambientando e criando familiaridade com os comandos e formas de atuar com o mecanismo de gerenciamento de repositório. Criando as estruturas de pasta e os arquivos necessários para o decorrer da trilha.

### Etapas para realização do desafio 
* Assistir as trilhas sobre o conteúdo
* Baixar arquivos necessários
* Instalar e utilizar os programas necessários
* Realizar teste, exercícios para conhecer e verificar as funcionalidades. 
* Adicionar convidado
* Criar arquivo em Markdown, e enviar para o repositório em locais específicos a estrutura de diretórios.

### Construção do desafio

Foi criada a estrutura de pastas, e em seguida criado o repositório no git hub, onde pelo comando git clone, atualização da maquina e envio das estruturas solicitadas.
[Conteúdo de pasta ao lado direito, e alguns trecho do envio para a nuvem.](/Sprint_01/evidencia/Screenshot_1.png).

Realizar a criação e preenchimento dos arquivos README, utilizando o Markdown.
[Exemplo de criação do arquivo em Markdown.](/Sprint_01/evidencia/Screenshot_2.png).

Realizar os upload de arquivos como, imagens, códigos, e outro.
[Upload arquivos.](/Sprint_01/evidencia/Screenshot_1.png).

E finalizando produzir um vídeo descritivo sobre as atividades realizadas na trilha e enviar o mesmo pelo aplicativo Stream
