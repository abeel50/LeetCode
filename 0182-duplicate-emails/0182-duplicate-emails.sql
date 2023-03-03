# Write your MySQL query statement below
select Email
from Person
group by 1
having count(1)>1