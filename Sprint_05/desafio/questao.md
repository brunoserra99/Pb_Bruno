# Seguindo execute estas manipulações:

* 1 - Uma Clausula que filtra dados usando ao menos dois operadores lógicos
* 2 - Duas funções de agregação
* 3 - Uma funções condicional
* 4 - Uma função de conversão
* 5 - Uma função de data
* 6 - Uma função de string


## Pergunta contendo os 6 itens:
Considerando as corridas com status 'Concluída' e quilometragem total maior que 5km, qual a média de km total das corridas, e qual valor total das corridas? Apresente o resultado após aplicar as seguintes transformações: criar uma coluna indicando se a corrida é 'longa' (km_total > 10), converter a coluna 'data_abertura' para o tipo data, extrair o dia da data de abertura, e apresentar os nomes de cidade em maiúsculos.

### Realizei o desafio seguindo esta lógica.

* 1 - Uma Clausula que filtra dados usando ao menos dois operadores lógicos
Foi utilizado o status de corrida concluída, e maior que 5km.

* 2 - Duas funções de agregação
Duas função usada, media do km das corridas, (corridas filtradas) e soma dos valores destas corridas

* 3 - Uma funções condicional
Condicionei corridas longas quando fosse acima de 10km, e curtas abaixo de 10km.

* 4 - Uma função de conversão
Foi convertido a coluna data de string para datetime, para no próximo itens manipular o dia.

* 5 - Uma função de data
Como as corridas era de últimos 7 dia retirou o dias para clareza ao resultado.

* 6 - Uma função de string
E manipulei a string para que a mesma normalize no todo, em letras minúsculas.
