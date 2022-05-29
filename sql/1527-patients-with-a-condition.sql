-- Learning here was that using like we cant just say or like, we need to explicitly
-- name the column again. 
SELECT *
FROM Patients
WHERE conditions LIKE 'DIAB1%' OR conditions LIKE '% DIAB1%'