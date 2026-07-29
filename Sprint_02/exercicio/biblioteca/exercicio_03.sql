SELECT 
    COUNT(Livro.cod) AS quantidade,
    Editora.nome AS nome,
    Endereco.estado AS estado,
    Endereco.cidade AS cidade
FROM 
    Livro
JOIN 
    Editora ON Livro.editora = Editora.codEditora
JOIN 
    Endereco ON Editora.endereco = Endereco.codEndereco
GROUP BY 
    Editora.codEditora, Editora.nome, Endereco.estado, Endereco.cidade
ORDER BY 
    quantidade DESC
LIMIT 5;