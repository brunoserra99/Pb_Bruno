#!/bin/bash

#Comando para execultar
#27 15 * * *  /home/user/CompassUol/ecommerce/processamento_de_vendas.sh
#16-59/2 18 * * * /home/user/CompassUol/ecommerce/processamento_de_vendas.sh


#<<<<<<<<Inicio do programa de backup diario>>> 1 version

#crinado diretorio vendas e arquivos nescessario 
mkdir /home/user/CompassUol/ecommerce/vendas
    cp /home/user/CompassUol/ecommerce/dados_de_vendas.csv /home/user/CompassUol/ecommerce/vendas/dados_de_vendas.csv

#criando diretorio backup e arquivos nescessario
mkdir /home/user/CompassUol/ecommerce/vendas/backup
    cp /home/user/CompassUol/ecommerce/vendas/dados_de_vendas.csv /home/user/CompassUol/ecommerce/vendas/backup/dados-$(date +"%y%m%d").csv
    #renomeando arquivo backup
    mv /home/user/CompassUol/ecommerce/vendas/backup/dados-$(date +"%y%m%d").csv /home/user/CompassUol/ecommerce/vendas/backup/backup-dados-$(date +%Y%m%d).csv

#criando arquivo relatorio e gerando dados
#lancando data atual
echo "$(date +"%Y/%m/%d %H:%M")" >> /home/user/CompassUol/ecommerce/vendas/backup/relatorio-$(date +%Y%m%d).txt

#lancando dados primeira venda
awk 'NR==2 {print $5}' FS=',' /home/user/CompassUol/ecommerce/vendas/backup/backup-dados-$(date +%Y%m%d).csv >> /home/user/CompassUol/ecommerce/vendas/backup/relatorio-$(date +%Y%m%d).txt

#lancando dados ultima venda
awk 'END {print $5}' FS=',' /home/user/CompassUol/ecommerce/vendas/backup/backup-dados-$(date +%Y%m%d).csv >> /home/user/CompassUol/ecommerce/vendas/backup/relatorio-$(date +%Y%m%d).txt

#contador itens diferentes
awk 'NR > 1 {print $2}' FS=',' /home/user/CompassUol/ecommerce/vendas/backup/backup-dados-$(date +%Y%m%d).csv | sort | uniq | wc -l  >>  /home/user/CompassUol/ecommerce/vendas/backup/relatorio-$(date +%Y%m%d).txt

#--------------------
#lancar as linhas 2-11 para o arquivo relatorioyyymmdd.txt
awk 'NR>1 && NR<12' /home/user/CompassUol/ecommerce/vendas/backup/backup-dados-$(date +%Y%m%d).csv >> /home/user/CompassUol/ecommerce/vendas/backup/relatorio-$(date +%Y%m%d).txt

#gerando arquivo backup.zip
cp /home/user/CompassUol/ecommerce/vendas/backup/backup-dados-$(date +%Y%m%d).csv /home/user/CompassUol/ecommerce/vendas/backup/backup-dados-$(date +%Y%m%d).zip

#limpando dados temp backup-dados....csv
rm -f /home/user/CompassUol/ecommerce/vendas/backup/backup-dados-$(date +%Y%m%d).csv

#limpando dados temp dados_de_vendas....csv
rm -f /home/user/CompassUol/ecommerce/vendas/dados_de_vendas.csv
