# Documentação do Projeto - Análise de Dados de Aplicativos do Google Play Store

## Descrição
Este projeto visa realizar uma análise exploratória de dados dos aplicativos disponíveis na Google Play Store, utilizando um arquivo CSV. Através da análise, foi possível realizar operações de limpeza de dados, gerar gráficos representativos e calcular estatísticas sobre as características dos aplicativos, como número de instalações, categorias e preços.

## Bibliotecas Utilizadas
- **Pandas**: Usada para manipulação de dados (leitura, limpeza e análise).
- **Matplotlib**: Usada para criação de gráficos.

## Funcionalidades

### 1. Remoção de Linhas Duplicadas
O primeiro passo foi ler o arquivo CSV e remover as linhas duplicadas. Isso é importante para garantir que a análise seja feita apenas com dados únicos. Após a remoção, o novo arquivo foi salvo em um novo CSV sem as duplicatas.

### 2. Gráfico de Barras - Top 5 Apps por Número de Instalações
Foi gerado um gráfico de barras horizontal mostrando os cinco aplicativos com o maior número de instalações. Para isso, a coluna de instalações foi limpa para remover caracteres não numéricos e convertida para inteiros. Depois, os aplicativos foram ordenados de forma decrescente pelo número de instalações e os 5 primeiros foram selecionados.

### 3. Gráfico de Pizza - Distribuição das Categorias de Apps
Foi criado um gráfico de pizza para representar a distribuição percentual das categorias de aplicativos presentes no dataset. A frequência das categorias foi contada e utilizada para gerar a visualização.

### 4. Aplicativo Mais Caro
Foi realizada a identificação do aplicativo mais caro da Play Store com base na coluna de preço. A coluna foi limpa para remover os símbolos de moeda e convertida para valores numéricos. Em seguida, foi encontrado o aplicativo com o maior valor de preço.

### 5. Contagem de Apps 'Mature 17+'
A contagem de aplicativos classificados como 'Mature 17+' foi realizada para entender a quantidade de aplicativos com essa classificação etária. Esse filtro foi feito através da coluna 'Content Rating'.

### 6. Top 10 Apps por Número de Reviews
Foi gerado um relatório dos 10 aplicativos com o maior número de avaliações (reviews). Os aplicativos foram ordenados de forma decrescente pelo número de reviews, e os 10 mais avaliados foram selecionados.

### 7. Cálculos Extras
Além dos cálculos e gráficos descritos acima, foram feitos outros cálculos, como:

- Total de reviews dos Top 10 aplicativos: A soma do número de reviews dos 10 aplicativos mais avaliados.
- Total de reviews de todos os aplicativos: A soma do número total de reviews no dataset.
- Média de reviews de todos os aplicativos: A média de reviews para todos os aplicativos presentes no dataset.

Além disso, os 3 aplicativos mais caros também foram identificados e a média de preço desses aplicativos foi calculada.

### 8. Gráficos Adicionais
Para complementar a análise, dois gráficos adicionais foram criados:

- **Gráfico de Linha (Line Plot)**: Representou a evolução do número de reviews dos top 10 aplicativos. Esse tipo de gráfico é útil para visualizar tendências ao longo de um conjunto de dados ordenado.
- **Gráfico de Dispersão (Scatter Plot)**: Representou a relação entre o preço e o número de reviews dos 3 aplicativos mais caros. Esse gráfico permite observar a dispersão entre essas duas variáveis para esses aplicativos específicos.

## Resultados Obtidos
- **Top 5 Apps por Número de Instalações**: O gráfico de barras revelou os 5 aplicativos com o maior número de instalações na Play Store.
- **Distribuição das Categorias de Apps**: O gráfico de pizza apresentou a distribuição percentual das categorias mais populares de aplicativos.
- **Aplicativo Mais Caro**: O aplicativo mais caro foi identificado, proporcionando insights sobre o preço máximo na loja.
- **Quantidade de Apps 'Mature 17+'**: Foi possível determinar quantos aplicativos são classificados para maiores de 17 anos.
- **Top 10 Apps por Número de Reviews**: Mostramos os aplicativos mais avaliados, ajudando a entender quais aplicativos têm maior interação com os usuários.
- **Média de Reviews**: A média de reviews de todos os aplicativos foi calculada, oferecendo uma visão geral sobre o nível de interações dos usuários com os aplicativos.
- **Apps Mais Caros e Média de Preço**: Foi possível identificar os aplicativos mais caros e calcular a média de seus preços.

## Conclusão
Este projeto demonstrou como é possível usar ferramentas como Pandas e Matplotlib para realizar uma análise exploratória de dados em datasets reais. Através de gráficos e cálculos, obtemos insights valiosos sobre os aplicativos da Google Play Store, como suas categorias, número de instalações, avaliações e preços. Essas informações podem ser úteis para desenvolvedores, analistas de mercado e outros interessados em entender melhor o comportamento dos aplicativos móveis.
