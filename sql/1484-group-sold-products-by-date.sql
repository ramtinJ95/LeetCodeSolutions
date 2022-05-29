-- Question asks not for number of products sold but rather number of DIFFRENT products
-- So this below does not solve that, the other solution fixes this by adding distinct in the count
SELECT 
    sell_date, 
    COUNT(product) AS num_sold, 
    GROUP_CONCAT(DISTINCT product ORDER BY product ASC) AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date ASC

SELECT 
    sell_date, 
    COUNT(DISTINCT product) AS num_sold, 
    GROUP_CONCAT(DISTINCT product ORDER BY product ASC) AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date ASC