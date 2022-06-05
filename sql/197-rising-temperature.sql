-- Datediff is super useful which I learned here.
-- Also comparing rows within the same table uses this selfjoin we did in the FROM
-- which was also new to me! 
SELECT
    w1.id
FROM Weather AS w1, Weather AS w2
WHERE w1.temperature > w2.temperature AND DATEDIFF(w1.recordDate, w2.recordDate) = 1