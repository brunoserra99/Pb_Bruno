# Sprint_10


Ao final da Sprint_10, me aprimorei mais em Python, já que esse foi assunto das sprints anteriores sprint_03 e sprint_04, sprint_05, sprint_06 e sprint_07, sprint_08, sprint_09 e sprint_10. Este assunto já foi estudado em outras oportunidades, mesmo como iniciante... Hoje posso dizer que possuo um conhecimento entre iniciante e intermediário.

Esta semana não foram apresentados cursos AWS, porém sigo estudando para a certificação, me aprimorando e me preparando para obter aprovação no exame AWS Certified Cloud Practitioner. Inclusive, já agendei a prova para a semana que vem.

Nesta sprint, foram dadas orientações sobre como realizar o agendamento da prova para a AWS Certified Cloud Practitioner, o qual foi marcado para a semana que vem. Também foi entregue um conteúdo introdutório ao termo "Storytelling" - a arte de contar histórias de forma envolvente. Esse aprendizado visa o desenvolvimento do dashboard para entrega do desafio, abrangendo a identificação do público, identidade visual e, no contexto geral, um estudo sobre "o que não fazer no QuickSight".

Tivemos um curso sobre o Amazon QuickSight, que é um serviço na nuvem que permite criar visualizações, analisar dados de diversas fontes e obter insights escaláveis com alto desempenho. Também aprendemos sobre a configuração da conta para construção do dashboard.

Foi realizada uma exploração mais prática do laboratório AWS, abordando algumas funções e serviços como S3, Athena, Lambda, Glue, IAM e QuickSight, demonstrando aplicações mais realistas e necessidades da vida real, simuladas nos laboratórios da AWS e no dia a dia do desenvolvedor.

Na parte de manipulação de dados dentro da AWS, trabalhamos com dados da camada refined para utilização no QuickSight, movendo os arquivos para a camada Trusted, colocando em prática a vivência e funcionalidades do dia a dia do analista de dados.

Essas duas semanas assistindo às videoaulas e realizando exercícios foram muito boas para aprofundar meus conhecimentos sobre as tecnologias que a AWS oferece.

O curso AWS mostrou exemplos de atividades utilizadas no cotidiano do profissional de TI, demonstrando sua utilidade de maneira prática e esclarecedora. Apesar de ser uma experiência breve, foi possível compreender de forma clara como se desenrola o dia a dia desses profissionais.

O desenvolvimento dos scripts foi realizado por meio da IDE VSCode, utilizando recursos com PySpark, Python e SQL, além de atividades dentro do AWS S3.

---

## Certificado do Curso da Sprint_10:

Esta sprint não teve cursos que geram certificados.

* [Não possui certificado](< >)

---

## Exercícios

Esta sprint não teve cursos e/ou exercícios específicos.

* [Não possui exercício](< >)

---

## Correção na(s) Sprint(s)

Após estudar e verificar o desenvolvimento presente e futuro do desafio, percebi que alguns dos meus dados não estavam sendo carregados corretamente, de acordo com o que havia sido feito no protótipo local. Após várias tentativas e modificações, optei por recomeçar e redefinir a construção do desafio.

Reformulei totalmente minha estratégia, refinando melhor o que iria analisar. Optei por analisar a franquia *Rocky*, que possui 6 filmes no total. A partir disso, gerei novas perguntas para realizar uma análise mais específica, reextraí os dados do TMDb para a camada RAW em arquivos JSON, converti os JSON para Parquet e ingeri os dados na camada Trusted. Após desenvolver o modelo de dados, realizei a ingestão na camada refined.

### Arquivo das questões:
* [Questões](../Sprint_07/desafio/questoes.md)

Evidência do trecho das questões corrigido:
![Evidência 01](<evidencias/1.png>)

### Extração de dados do TMDb para a camada RAW (.json)

Evidência do script modificado:
* [script(correcao_sprint).py](desafio/correcao_sprint/script_extracao_tmdb.py)

Evidência dos arquivos gerados:
![Evidência 02](<evidencias/2.png>)

> ***Lembrando que o arquivo foi alterado para manter as credenciais em segurança. No local das credenciais, foi adicionado: id_xxx***

### Conversão da camada RAW (.json) para Trusted (.parquet)

Evidência do script modificado:
* [script(correcao_sprint).py](desafio/correcao_sprint/script_raw_trusted.py)

Evidência rodando o *crawler*:
![Evidência 03](<evidencias/3.png>)

Evidência dos arquivos gerados:
![Evidência 04](<evidencias/4.png>)

### Modelo de Dados

Evidência do trecho do código corrigido:
![Evidência Modelo de Dados](<evidencias/rocky_modelo_dados.png>)

### Finalização para a camada Refined (.parquet)

Evidência do script modificado:
* [script(correcao_sprint).py](desafio/correcao_sprint/script_trusted_refined.py)

Evidência rodando o *crawler*:
![Evidência 05](<evidencias/5.png>)

Evidência dos arquivos gerados:
![Evidência 06](<evidencias/6.png>)
![Evidência 07](<evidencias/7.png>)

 ***A partir daí, foi dada sequência à Sprint_10.

 ***Como não sabia onde colocar esta correção, optei por criar uma nova pasta dentro do desafio e adicionar as correções de script. As evidências seguem na pasta de evidências.

---

## Desafio

Entrego os códigos que foram criados para o desenvolvimento do desafio.

Início o desafio realizando a configuração do ambiente AWS Glue. A partir desse ambiente, desenvolvo o ambiente Athena e, em seguida, configuro as credenciais no QuickSight e desenvolvo o dashboard.

Evidência da configuração no QuickSight:
![Evidência 08](<evidencias/500$_Captura de tela.png>)

Evidência dos arquivos datasets no QuickSight:
![Evidência 09](<evidencias/9.png>)

Evidência do dashboard finalizado:
![Dashboard Finalizado](<evidencias/dashboard.png>)

No readme do desafio irei descrever a representacao do dashboard e outros assuntos.

---

### Desafio finalizado

> ***Também foi alterado o arquivo contendo as credenciais, que foram substituídas por id_XXXX.***

