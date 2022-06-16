-- Good way
SELECT Email
FROM Person
GROUP BY Email
HAVING COUNT(*) > 1

-- Using self join trick i recently learned
SELECT DISTINCT a.email AS Email
FROM Person AS a, Person AS b
WHERE a.email = b.email AND a.id != b.id