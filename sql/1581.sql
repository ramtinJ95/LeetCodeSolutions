SELECT 
    customer_id, 
    count(Visits.visit_id) as count_no_trans 
FROM Visits
LEFT JOIN Transactions
ON Transactions.visit_id = Visits.visit_id 
WHERE Transactions.visit_id IS NULL
GROUP BY customer_id
