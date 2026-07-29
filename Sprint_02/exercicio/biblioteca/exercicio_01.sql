--busca de publicados apartir de 2014
SELECT cod, titulo, autor, editora, valor, publicacao, edicao, idioma
FROM livro
WHERE publicacao > '2014-12-31'
ORDER BY cod asc;