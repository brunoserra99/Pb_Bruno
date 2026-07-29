SELECT
    estado,
    nmpro AS nmpro,
    ROUND(AVG(qtd), 4) AS quantidade_media
FROM
    tbvendas
WHERE
    status = 'Concluído'
GROUP BY
    estado, nmpro
ORDER BY
    estado ASC, nmpro ASC;