SELECT 
    v.cdvdd, 
    v.nmvdd
FROM 
    tbvendas AS vendas
JOIN 
    tbvendedor AS v ON vendas.cdvdd = v.cdvdd
WHERE 
    vendas.status = 'Concluído'
GROUP BY 
    v.cdvdd, v.nmvdd
ORDER BY 
    COUNT(vendas.cdven) DESC
LIMIT 1;