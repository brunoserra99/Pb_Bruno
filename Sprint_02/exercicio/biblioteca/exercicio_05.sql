SELECT DISTINCT a.nome
FROM autor a
JOIN livro l ON a.codAutor = l.autor
JOIN editora e ON l.editora = e.codEditora
JOIN endereco en ON e.endereco = en.codEndereco
WHERE en.estado NOT IN ('PARANÁ', 'RIO GRANDE DO SUL', 'SANTA CATARINA')
ORDER BY a.nome ASC;