# Write your MySQL query statement below
select e.employee_id
    from Employees e
    left join Salaries s
    ON s.employee_id = e.employee_id
    where s.salary is null
union all
select s.employee_id
    from Employees e
    right join Salaries s
    ON s.employee_id = e.employee_id
    where e.name is null
order by employee_id;
    