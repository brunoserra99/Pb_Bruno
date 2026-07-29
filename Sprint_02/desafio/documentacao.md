## 1. Tabelas Dimensionais
As tabelas dimensionais contêm dados descritivos e são referenciadas pela tabela fato. Cada tabela dimensional armazena dados únicos de uma entidade.

## 1.1 dimensao_cliente
Tabela que armazena informações sobre os clientes.

•	Colunas:

*	id_cliente: Identificador único do cliente (chave primária).
*	nome_cliente: Nome do cliente.
*	cidade_cliente: Cidade do cliente.
*	estado_cliente: Estado do cliente.
*	pais_cliente: País do cliente.
Inserção de Dados: Os dados são preenchidos a partir da tabela tb_locacao, extraindo informações únicas dos clientes.

### 1.2 dimensao_carro
Tabela que armazena informações sobre os carros.

•	Colunas:

*	km_carro: Quilometragem do carro.
*	classificacao_carro: Classificação do carro (categoria).
*	marca_carro: Marca do carro.
*	modelo_carro: Modelo do carro.
*	ano_carro: Ano de fabricação do carro.
Inserção de Dados: Dados únicos dos carros são selecionados da tb_locacao, extraindo a quilometragem máxima (kmCarro) registrada para cada carro.

### 1.3 dimensao_combustivel
Tabela que armazena informações sobre os tipos de combustível.

### Colunas:

*	id_combustivel: Identificador único do tipo de combustível (chave primária).
*	tipo_combustivel: Tipo de combustível utilizado (Etanol., Gasolina, Diesel).
Inserção de Dados: Os dados são preenchidos a partir de registros distintos na tb_locacao.

### 1.4 dimensao_vendedor
Tabela que armazena informações sobre os vendedores.

•	Colunas:

*	id_vendedor: Identificador único do vendedor (chave primária).
*	nome_vendedor: Nome do vendedor.
*	sexo_vendedor: Gênero do vendedor (0 para feminino, 1 para masculino).
*	estado_vendedor: Estado de atuação do vendedor.
Inserção de Dados: Dados únicos dos vendedores são extraídos da tabela tb_locacao.

## 2. Tabela Fato
A tabela fato (fato_locacao) armazena eventos de locação, associando as tabelas dimensionais.

### 2.1 fato_locacao
Tabela que registra cada locação de carro, incluindo referências às tabelas dimensionais e informações de locação.

•	Colunas:

*	id_locacao: Identificador único da locação (chave primária).
*	id_cliente: Chave estrangeira para dimensao_cliente.
*	id_carro: Chave estrangeira para dimensao_carro.
*	id_combustivel: Chave estrangeira para dimensao_combustivel.
*	id_vendedor: Chave estrangeira para dimensao_vendedor.
*	data_locacao: Data da locação.
*	hora_locacao: Hora da locação.
*	qtd_diaria: Quantidade de diárias contratadas.
*	vlr_diaria: Valor da diária.
*	data_entrega: Data de entrega do carro.
*	hora_entrega: Hora de entrega do carro.
Inserção de Dados: Os dados da tabela fato são preenchidos diretamente da tabela tb_locacao, incluindo informações detalhadas de cada locação.

## 3. Views para Análise
As views facilitam a análise dos dados de locação e de data de locação.
### 3.1 view_data_locacao
View que transforma data_locacao em componentes de ano, mês, semana e dia para análise temporal.

•	Colunas:

*	data: Data completa da locação.
*	ano: Ano da locação.
*	mes: Mês da locação.
*	semana: Semana do ano da locação.
*	dia: Dia do mês da locação.

### 3.2 view_analise_locacoes
View que combina informações das tabelas dimensionais e da tabela fato para uma visão completa das locações.

•	Colunas:

*	data_locacao: Data da locação.
*	qtd_diaria: Quantidade de diárias.
*	vlr_diaria: Valor da diária.
*	nome_cliente: Nome do cliente.
*	cidade_cliente: Cidade do cliente.
*	marca_carro: Marca do carro alugado.
*	modelo_carro: Modelo do carro alugado.
*	tipo_combustivel: Tipo de combustível do carro.
*	nome_vendedor: Nome do vendedor responsável pela locação.
