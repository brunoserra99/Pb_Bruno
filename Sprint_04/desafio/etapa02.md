# Etapa 02 - Desafio Docker

## Pergunta:
### É possível reutilizar containers? Em caso positivo, apresente o comando necessário para reiniciar um dos containers parados em seu ambiente Docker? Não sendo possível reutilizar, justifique a sua resposta.

## Resposta
Sim, e possível reutilizar container pausado ou parado no meu ambiente. Para reiniciar:
docker start id_container

### obs.:
Caso o contêiner tenha sido removido/apagado ou corrompido não será possível. Será necessário criar outro a partir da imagem:
docker run id_imagem

#### Substitua o id_container e/ou id_imagem, pelo nome o qual deseja inicializar ou criar/executar.
