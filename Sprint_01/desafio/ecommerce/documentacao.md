# Documentação do programa gerador de backup

## Programa BackupsScriptsOne

## 1. Objetivo
Este programa automatiza o processamento diário de um arquivo _dados_de_vendas.csv_  localizado no diretório _home/ecommerce_. Ele realiza operações como cópia, extração de dados, contagem de produtos e compactação dos arquivos para facilitar o gerenciamento de vendas.

## 2. Requisitos
* Sistema operacional: Linux.
* Linguagem/Script de programação: Bash / Shell script.
* Permissões de leitura e escrita nos diretórios especificados.
* Crontab para agendamento de execução diária.

## 3. Uso
O programa é executado automaticamente todos os dias às 15h27 através de uma tarefa/script crontab. Para configurar, adicione a seguinte linha no crontab:

#### 27 15 * * * home/ecommerce/processamento_de_vendas.sh

## 4. Funcionamento
* Criação de Diretórios e Copia de Dados: O programa cria os diretórios _home/ecommerce/**vendas**_ e copia o arquivo _home/ecommerce/**dados_de_vendas.csv**_ para o diretorio _home/ecommerce/**vendas/dados_de_vendas.csv**_.
Em seguida cria o dirertorio _home/ecommerce/vendas/**backup**_ e copia o arquivo _home/ecommerce/**vendas/dados_de_vendas.csv**_ para _home/ecommerce/vendas/**backup/**_ alterando o nome do arquivo para ..._**dados-yyyymmdd.csv**_.
Finalizando dentro do diretório _home/ecommerce/vendas/backup/_ ocorre a transição do nome do arquivo _dados-YYYYMMDD.csv_ para o nome de _backup-dados-YYYYMMDD.csv_.
* Extração de Dados: O programa lê o arquivo _home/ecommerce/vendas/backup/backup-dados-YYYYMMDD.csv_ em  seguida ele cria um novo arquivo _...vendas/bakup/relatorioYYYYMMDD.txt_ inserindo a _data atual, data do primeiro registro de  venda,  data do ultimo registro de venda, e quantidade total de itens diferentes vendidos_.
* Compactação: O arquivo _backup-dados-YYYYMMDD.csv_  é compactado e salvo como _home/ecommerce/vendas/backup/backup-dados-YYYYMMDD.zip_ .
* Finalizando o programa realiza a limpeza de dados temporário apagando _home/ecommerce/vendas/backup/backup-dados-YYYYMMDD.csv_ e o _home/ecommerce/vendas/dados_de_vendas.csv_

## 5. Exemplos

* Criação do diretório: _mkdir home/ecommerce/vendas_.
* Cópia do arquivo: _cp /home/ecommerce/dados_de_vendas.csv /home/ecommerce/vendas /backup/dados-$(date +"%y%m%d").csv_
* Extração de dados e contagem de produtos: _Awk ‘NR==2 {print $5}' FS=',' /home/ecommerce/vendas/backup/ backup-dados-$(date +%Y%m%d).csv >> /home/ecommerce/vendas/ backup/relatorio-$(date +%Y%m%d).txt_

## 6. Manutenção
Atualizações: Sempre que o formato do arquivo _dados_de_vendas.csv_ mudar, revise o código para garantir que a extração de dados funcione corretamente.

## 7. Conclusão
Este programa proporciona uma maneira eficiente de gerenciar e processar dados de vendas diariamente, garantindo que as informações sejam consolidadas e armazenadas adequadamente para análises futuras.

## 8. Append
A primeira vez que o programa rodou no cliente/servidor/maquina, ocorreu, falha na transcrição de dados da ultima venda, devido conter linha em branco no final do documento, a primeira correção foi deletar manualmente a linha em branco e assim resolver o problema. E em seguida arrumar o código para consegui rodar corretamente. Gerando a versão 1.1 do programa.