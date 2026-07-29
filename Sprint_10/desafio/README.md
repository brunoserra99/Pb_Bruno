# Desafio sprint_10

### Objetivo

Familiarização com a linguagem Python, biblioteca pandas e boto3, laboratório como S3, Athena, Crawler, Lambda, Glue, IAM e QuickSight, e o serviço AWS no geral, além da manipulação de arquivos no AWS S3. Aprendizado sobre o ambiente AWS e a utilização dos comandos para upload, download, criação e execução de buckets no ambiente AWS, além de funções no Lambda e Glue, entre outras.

### Descrição

Desenvolver configurações para o manuseio do QuickSight, usando a base de dados da camada Refined, e assim consumir os dados para o desenvolvimento de um dashboard, para que fossem respondidas as questões geradas anteriormente e realizada a apresentação do mesmo. Gerando e simulando experiências próximas da realidade, para aprendizado sobre os assuntos. Entregar tudo de maneira organizada no repositório do GitHub.

### Etapas para realização do desafio

* Criar e desenvolver o script em Python
* Utilizar as bibliotecas solicitadas
* Configurar serviços AWS
* Utilização de serviços AWS em conjunto como S3, Athena, QuickSight
* Finalizar arquivo e estruturas a serem entregues
* Finalizar no repositório do GitHub

### Correção do arquivo JSON

Como relatado no README da sprint_10, devido a um melhor entendimento do que foi solicitado, foi necessário refazer a extração de dados do TMDb, pois os mesmos não haviam capturado os dados necessários.

### Construção do desafio

Foi iniciada a configuração do QuickSight, seguindo orientações conforme estavam na documentação fornecida, gerando permissões para que o QuickSight pudesse, por meio do Athena, consumir os dados da camada Refined no bucket S3. Dessa maneira, por meio do dashboard, gerar a apresentação visual que seria entregue.

## Desafio

Entrego os códigos que foram criados para o desenvolvimento do desafio.

Iniciei o desafio realizando a configuração do Athena e, em seguida, configurei as credenciais no QuickSight, consumi a base de dados da camada Refined com o QuickSight e desenvolvi o dashboard.

Evidência da configuração no QuickSight:
![Evidência 08](<../evidencias/500$_Captura de tela.png>)

Evidência do dashboard finalizado:
![Dashboard Finalizado](<../evidencias/dashboard.png>)

### Descrição do dashboard

Ao desenvolver a linha de pensamento para a criação do dashboard, uma das perguntas que ecoaram em minha mente foi o quanto lucrativos os filmes da franquia Rocky foram, e quais outras características poderiam ser aproveitadas, e se o modelo de como foi gerida essa franquia foi vitorioso ou não. E para responder a essas questões, nada mais fidedigno que os números que fazem parte desse enredo.

Evidência da configuração no QuickSight:
![Evidência 09](<../evidencias/img_top.png>)

Acima temos uma imagem com o título e alguns insights que representam a vitória e deixam claro praticamente o que se quer dizer no dashboard, mantendo assim a atenção e o foco no conteúdo.

Logo abaixo, ao centro, temos um gráfico mostrando os títulos da franquia, dando ênfase ao nome "Rocky" (em vermelho). À esquerda, temos um valor de orçamento nítido e claro, de quanto foi gasto (122 milhões). E à direita, temos o número de receita também nítido e claro de quanto foi lucrado. Neste enredo, o primeiro número (precedido da vírgula) pode até se passar despercebido, mas é um claro diferencial sobre os dados, gerando 1 bilhão de motivos para isso.

![Evidência 10](<../evidencias/10.png>)

Agora que já esclarecemos e pontuamos que os valores estão na casa do bilhão, acima e à esquerda temos o resultado líquido obtido com a franquia e todos os seus filmes: 1 bilhão e alguns milhões (1.034 milhões).

Ao lado direito do lucro líquido, apresentamos o valor em porcentagem sobre o orçamento, onde o lucro foi de quase 850% do que foi investido. Sim, para cada dólar investido, retornaram aproximadamente 848 dólares. Seguindo acima e à direita, temos talvez o principal motivo para que esses valores fossem obtidos: a média da nota de todos os filmes, onde Rocky Balboa superou seus limites. Agradando ao público, obteve uma nota média de 6,96, um "sete" ok?

Números expressivos para a franquia, respondendo assim as perguntas citadas no começo da descrição. Em resumo, sim, a franquia de filmes Rocky não só fez sucesso, como também gerou uma fortuna em lucros, e tudo isso com qualidade para seus espectadores.

Com esses dados, já seria uma ótima opção um investimento para o próximo filme.

Abaixo, temos no gráfico bege os filmes e seus orçamentos. O primeiro Rocky teve um investimento na casa de 1 milhão de dólares, isso há quase 50 anos atrás. Rocky V, há aproximadamente 30 anos, teve um investimento na casa dos 42 milhões, sem um investimento maior que Rocky Balboa, filme de 2006, cujo investimento foi de aproximadamente 25 milhões.

Ao lado, na cor laranja, temos a receita gerada pelos filmes. Note que Rocky Balboa, o último filme produzido, gerou um retorno bruto de aproximadamente 150 milhões, um valor muito maior que o investido, sendo altamente lucrativo mesmo com a concorrência de hoje em dia. Até mesmo Rocky V, que teve um altíssimo orçamento, gerou um grande valor de retorno, onde os seus 40 milhões investidos retornaram na casa de 120 milhões. O primeiro filme da série Rocky, com seu orçamento de 1 milhão, retornou mais de 220 milhões de lucro. E assim se tornando o sucesso, como um dos clássicos filmes já produzidos.

![Evidência 11](<../evidencias/11.png>)

Segue os gráficos ROI e votos por filme.

![Evidência 12](<../evidencias/12.png>)

Acima, à esquerda, temos o gráfico ROI - Retorno de Investimento, um gráfico importantíssimo para comparação, onde pode ser números positivos ou negativos. O filme Rocky teve um ROI de mais de 22 mil, sendo uma excelente métrica para comparação. O filme que menos pontuou nesse quesito foi Rocky V, com 185 pontos, e Rocky Balboa com 549 pontos, mostrando como os filmes foram bons para o retorno de investimento.

E seguindo, à direita, temos os valores que mostram os votos que cada título recebeu, onde praticamente todos receberam 4 mil votos, e apenas Rocky recebeu o dobro de votos, algo em torno de 8 mil votos.

Finalizando, temos um comparativo de duração, orçamento e receita, e, à direita, um comparativo de nota média, orçamento e receita.

![Evidência 13](<../evidencias/13.png>)

Neste gráfico, são representados por uma coluna à esquerda com o orçamento e uma linha abaixo com a receita. No gráfico à direita, temos os pontos representando a duração em minutos. Os filmes com menor orçamento foram os mais longos, e o primeiro filme produzido, Rocky, conseguiu um ótimo retorno financeiro como explicado acima.

Já no gráfico à direita, temos os pontos representando as notas médias. Novamente, Rocky foi o filme com uma das maiores notas. Mesmo com baixo investimento e um grande retorno, teve uma nota de 7,79. No contexto geral, todos tiveram notas acima de 6,9. Apenas Rocky V, com uma nota abaixo de 6, obteve 5.8, podendo ser o motivo pelo qual o filme não obteve uma excelente taxa de retorno de investimento (ROI), justificando o porquê o filme com maior investimento obteve um retorno menor que 4 filmes da franquia, ficando à frente apenas de Rocky II, cujo investimento não chegou aos 10 milhões, porém seu lucro foi na casa de 85 milhões.

Evidência do dashboard na íntegra:
![Dashboard na íntegra](<../evidencias/dashboard.png>)

---

### Desafio finalizado

> ***Também foi alterado o arquivo contendo as credenciais, que foram substituídas por id_XXXX.***
