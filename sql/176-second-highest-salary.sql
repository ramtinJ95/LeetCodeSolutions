SELECT 
    IFNULL
    (
        (
            SELECT 
                DISTINCT salary 
            FROM employee 
            ORDER BY salary DESC LIMIT 1,1
        )
        ,
        NULL
    ) AS SecondHighestSalary