SELECT
    nmvdd AS vendedor,
    SUM(vd.qtd * vd.vrunt) AS valor_total_vendas,
    CASE
        WHEN (SUM(vd.qtd * vd.vrunt) * ve.perccomissao / 100) = 1 THEN 
            ROUND(SUM(vd.qtd * vd.vrunt) * ve.perccomissao / 100 / 2, 2)
        ELSE 
            ROUND(SUM(vd.qtd * vd.vrunt) * ve.perccomissao / 100, 2)
    END AS comissao
FROM
    tbvendas vd
JOIN
    tbvendedor ve ON vd.cdvdd = ve.cdvdd
WHERE
    vd.status = 'Concluído'
GROUP BY
    nmvdd, ve.perccomissao
ORDER BY
    comissao DESC;