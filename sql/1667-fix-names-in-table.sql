-- never worked with strings in sql, surprised there are such powerful built in stuff!
SELECT user_id, CONCAT(UPPER(SUBSTRING(name, 1,1)), LOWER(SUBSTRING(name, 2))) as name
FROM Users
ORDER BY user_id ASC