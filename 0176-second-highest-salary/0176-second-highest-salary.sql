# Write your MySQL query statement below
SELECT
    MAX(salary) as SecondHighestSalary
FROM
    Employee
WHERE
    salary < (SELECT 
                MAX(Salary)   
              FROM
                Employee)