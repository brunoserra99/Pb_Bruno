select a.nome
from autor a
left join livro l on a.codautor = l.autor
where l.cod is null
order by a.nome;