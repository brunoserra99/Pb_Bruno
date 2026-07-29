-- criação das tabela fato/dimensionais

-- criação das tabela dimensao_cliente
create table if not exists dimensao_cliente (
    id_cliente integer primary key,
    nome_cliente varchar not null,
    cidade_cliente varchar,
    estado_cliente varchar,
    pais_cliente varchar
);
--select * from dimensao_cliente;

-- criação das tabela dimensao_carro
create table if not exists dimensao_carro (
    id_carro integer primary key,
    km_carro integer,
    classificacao_carro varchar,
    marca_carro varchar,
    modelo_carro varchar,
    ano_carro integer
);
--select * from dimensao_carro;

-- criação das tabela dimensao_combustivel
create table if not exists dimensao_combustivel (
    id_combustivel integer primary key,
    tipo_combustivel varchar not null
);
--select * from dimensao_combustivel ;

-- criação das tabela dimensao_vendedor
create table if not exists dimensao_vendedor (
    id_vendedor integer primary key,
    nome_vendedor varchar not null,
    sexo_vendedor smallint,
    estado_vendedor varchar
);
--select * from dimensao_vendedor dv ;


-- criação das tabela fato_locacao
create table if not exists fato_locacao (
    id_locacao integer primary key, 
    id_cliente integer not null, 
    id_carro integer not null, 
    id_combustivel integer not null, 
    id_vendedor integer not null, 
    data_locacao datetime, 
    hora_locacao time, 
    qtd_diaria integer, 
    vlr_diaria decimal, 
    data_entrega date, 
    hora_entrega time,
    foreign key (id_cliente) references dimensao_cliente(id_cliente),
    foreign key (id_carro) references dimensao_carro(id_carro),
    foreign key (id_combustivel) references dimensao_combustivel(id_combustivel),
    foreign key (id_vendedor) references dimensao_vendedor(id_vendedor)
);

-- Inserção de dados nas tabelas dimensionais
-- criação das tabela dimensao_cliente
insert into dimensao_cliente (id_cliente, nome_cliente, cidade_cliente, estado_cliente, pais_cliente)
select distinct idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente from tb_locacao;

-- criação das tabela dimensao_carro
insert into dimensao_carro (id_carro, km_carro, classificacao_carro, marca_carro, modelo_carro, ano_carro)
select distinct idCarro, max(kmCarro), classiCarro, marcaCarro, modeloCarro, anoCarro from tb_locacao;

-- criação das tabela dimensao_combustivel
insert into dimensao_combustivel (id_combustivel, tipo_combustivel)
select distinct idCombustivel, tipoCombustivel from tb_locacao;

-- criação das tabela dimensao_vendedor
insert into dimensao_vendedor (id_vendedor, nome_vendedor, sexo_vendedor, estado_vendedor)
select distinct idVendedor, nomeVendedor, sexoVendedor, estadoVendedor from tb_locacao;

-- Inserção de dados na tabela fato_locacao
insert into fato_locacao (id_locacao, id_cliente, id_carro, id_combustivel, id_vendedor, data_locacao, hora_locacao, qtd_diaria, vlr_diaria, data_entrega, hora_entrega)
select idLocacao, idCliente, idCarro, idCombustivel, idVendedor, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega from tb_locacao;

--select * from dimensao_carro dc  ;

-- Criação das views para análise

-- Visualização da data de locação
create view if not exists view_data_locacao as
select distinct
    data_locacao as data,
    strftime('%Y', data_locacao) as ano,
    strftime('%m', data_locacao) as mes,
    strftime('%W', data_locacao) as semana,
    strftime('%d', data_locacao) as dia
from fato_locacao;
select * from view_data_locacao vdl ;

-- Visualização para análise de locações
create view if not exists view_analise_locacoes as
select 
    fato_locacao.data_locacao,
    fato_locacao.qtd_diaria,
    fato_locacao.vlr_diaria,
    dimensao_cliente.nome_cliente,
    dimensao_cliente.cidade_cliente,
    dimensao_carro.marca_carro,
    dimensao_carro.modelo_carro,
    dimensao_combustivel.tipo_combustivel,
    dimensao_vendedor.nome_vendedor
from fato_locacao
join dimensao_cliente on fato_locacao.id_cliente = dimensao_cliente.id_cliente
join dimensao_carro on fato_locacao.id_carro = dimensao_carro.id_carro
join dimensao_combustivel on fato_locacao.id_combustivel = dimensao_combustivel.id_combustivel
join dimensao_vendedor on fato_locacao.id_vendedor = dimensao_vendedor.id_vendedor;


