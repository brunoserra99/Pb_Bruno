WITH vendedor_com_vendas AS (
    SELECT 
        cdvdd,
        SUM(qtd * vrunt) AS total_vendas
    FROM 
        tbvendas
    WHERE 
        status = 'Concluído'
    GROUP BY 
        cdvdd
    HAVING 
        SUM(qtd * vrunt) > 0  -- Excluir vendedores com vendas zero
),
menor_vendedor AS (
    SELECT 
        cdvdd
    FROM 
        vendedor_com_vendas
    ORDER BY 
        total_vendas ASC
    LIMIT 1
)
SELECT 
    d.cddep,
    d.nmdep,
    d.dtnasc,
    ROUND(SUM(v.qtd * v.vrunt), 2) AS valor_total_vendas
FROM 
    tbdependente d
JOIN 
    tbvendas v ON d.cdvdd = v.cdvdd
WHERE 
    d.cdvdd = (SELECT cdvdd FROM menor_vendedor) 
    AND v.status = 'Concluído'
GROUP BY 
    d.cddep, d.nmdep, d.dtnasc
ORDER BY 
    d.cddep;
